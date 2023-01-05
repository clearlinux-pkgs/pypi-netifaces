#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-netifaces
Version  : 0.11.0
Release  : 84
URL      : https://files.pythonhosted.org/packages/a6/91/86a6eac449ddfae239e93ffc1918cf33fd9bab35c04d1e963b311e347a73/netifaces-0.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/91/86a6eac449ddfae239e93ffc1918cf33fd9bab35c04d1e963b311e347a73/netifaces-0.11.0.tar.gz
Summary  : Portable network interface information.
Group    : Development/Tools
License  : MIT
Requires: pypi-netifaces-filemap = %{version}-%{release}
Requires: pypi-netifaces-lib = %{version}-%{release}
Requires: pypi-netifaces-license = %{version}-%{release}
Requires: pypi-netifaces-python = %{version}-%{release}
Requires: pypi-netifaces-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
================
        
        +-------------+------------------+
        | Linux/macOS | |BuildStatus|    |
        +-------------+------------------+
        | Windows     | |WinBuildStatus| |
        +-------------+------------------+

%package filemap
Summary: filemap components for the pypi-netifaces package.
Group: Default

%description filemap
filemap components for the pypi-netifaces package.


%package lib
Summary: lib components for the pypi-netifaces package.
Group: Libraries
Requires: pypi-netifaces-license = %{version}-%{release}
Requires: pypi-netifaces-filemap = %{version}-%{release}

%description lib
lib components for the pypi-netifaces package.


%package license
Summary: license components for the pypi-netifaces package.
Group: Default

%description license
license components for the pypi-netifaces package.


%package python
Summary: python components for the pypi-netifaces package.
Group: Default
Requires: pypi-netifaces-python3 = %{version}-%{release}

%description python
python components for the pypi-netifaces package.


%package python3
Summary: python3 components for the pypi-netifaces package.
Group: Default
Requires: pypi-netifaces-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(netifaces)

%description python3
python3 components for the pypi-netifaces package.


%prep
%setup -q -n netifaces-0.11.0
cd %{_builddir}/netifaces-0.11.0
pushd ..
cp -a netifaces-0.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672292614
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
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
#PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 test.py

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-netifaces
cp %{_builddir}/netifaces-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-netifaces/d2974c6505102e9199d25bd4c993bfcceafbdf2e || :
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-netifaces

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-netifaces/d2974c6505102e9199d25bd4c993bfcceafbdf2e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
