# Conditional build:
%bcond_without  tests   # do not perform "make test"

%define __python /usr/bin/python26
%define py_sitescriptdir /usr/lib/python2.6/site-packages/
%define     module  keyczar
Summary:    Toolkit for safe and simple cryptography
Name:       python26-%{module}
Version:    0.71c
Release:    1
License:    Apache v2.0
Group:      Development/Languages
Source0:    http://keyczar.googlecode.com/files/python-%{module}-%{version}.tar.gz
# Source0-md5:  57154b1e8ad3f59e2c8296d5d5a516eb
URL:        http://www.keyczar.org/
BuildRequires:  python26-crypto
BuildRequires:  python26-devel
BuildRequires:  python26-pyasn1
Requires:   python26-crypto
Requires:   python26-pyasn1
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%prep
%setup -q -n python-%{module}-%{version}
rm -r python_keyczar.egg-info

%build
%{__python} setup.py build

%if %{with tests}
cd tests/keyczar_tests
PYTHONPATH=$PYTHONPATH:../../src/ %{__python} ./alltests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
    --skip-build \
    --optimize=2 \
    --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc/pycrypt.pdf
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/python_keyczar-*.egg-info
