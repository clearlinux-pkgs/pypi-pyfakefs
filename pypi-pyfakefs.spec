#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyfakefs
Version  : 4.7.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/b0/1d/eabab46c2f441092cf9e989da72cbf15cc470fbbb03a73a97cc99dd8c6cf/pyfakefs-4.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/1d/eabab46c2f441092cf9e989da72cbf15cc470fbbb03a73a97cc99dd8c6cf/pyfakefs-4.7.0.tar.gz
Summary  : pyfakefs implements a fake file system that mocks the Python file system modules.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pyfakefs-license = %{version}-%{release}
Requires: pypi-pyfakefs-python = %{version}-%{release}
Requires: pypi-pyfakefs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# pyfakefs [![PyPI version](https://badge.fury.io/py/pyfakefs.svg)](https://badge.fury.io/py/pyfakefs) [![Python version](https://img.shields.io/pypi/pyversions/pyfakefs.svg)](https://img.shields.io/pypi/pyversions/pyfakefs.svg) ![Testsuite](https://github.com/jmcgeheeiv/pyfakefs/workflows/Testsuite/badge.svg)

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
%setup -q -n pyfakefs-4.7.0
cd %{_builddir}/pyfakefs-4.7.0
pushd ..
cp -a pyfakefs-4.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663601085
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyfakefs
cp %{_builddir}/pyfakefs-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyfakefs/89608a8f5632e1430c94fc5725a8aaea1a106ba6 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
