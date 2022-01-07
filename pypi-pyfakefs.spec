#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyfakefs
Version  : 4.5.3
Release  : 3
URL      : https://files.pythonhosted.org/packages/73/86/c8a0c50e5cbdfa14beec1dfa5a38b30614eae87d663103e1f2682d389bc5/pyfakefs-4.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/73/86/c8a0c50e5cbdfa14beec1dfa5a38b30614eae87d663103e1f2682d389bc5/pyfakefs-4.5.3.tar.gz
Summary  : pyfakefs implements a fake file system that mocks the Python file system modules.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pyfakefs-license = %{version}-%{release}
Requires: pypi-pyfakefs-python = %{version}-%{release}
Requires: pypi-pyfakefs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
pyfakefs implements a fake file system that mocks the Python file system modules.
        Using pyfakefs, your tests operate on a fake file system in memory without
        touching the real disk.  The software under test requires no modification to
        work with pyfakefs.
        
        pyfakefs works with Linux, Windows and MacOS.
        
        ## Documentation

%package license
Summary: license components for the pypi-pyfakefs package.
Group: Default

%description license
license components for the pypi-pyfakefs package.


%package python
Summary: python components for the pypi-pyfakefs package.
Group: Default
Requires: pypi-pyfakefs-python3 = %{version}-%{release}

%description python
python components for the pypi-pyfakefs package.


%package python3
Summary: python3 components for the pypi-pyfakefs package.
Group: Default
Requires: python3-core
Provides: pypi(pyfakefs)

%description python3
python3 components for the pypi-pyfakefs package.


%prep
%setup -q -n pyfakefs-4.5.3
cd %{_builddir}/pyfakefs-4.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639042644
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyfakefs
cp %{_builddir}/pyfakefs-4.5.3/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyfakefs/89608a8f5632e1430c94fc5725a8aaea1a106ba6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyfakefs/89608a8f5632e1430c94fc5725a8aaea1a106ba6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
