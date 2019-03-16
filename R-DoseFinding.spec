#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DoseFinding
Version  : 0.9.16
Release  : 6
URL      : https://cran.r-project.org/src/contrib/DoseFinding_0.9-16.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DoseFinding_0.9-16.tar.gz
Summary  : Planning and Analyzing Dose Finding Experiments
Group    : Development/Tools
License  : GPL-3.0
Requires: R-DoseFinding-lib
Requires: R-mvtnorm
BuildRequires : R-mvtnorm
BuildRequires : clr-R-helpers

%description
of dose-finding experiments (with focus on pharmaceutical Phase

%package lib
Summary: lib components for the R-DoseFinding package.
Group: Libraries

%description lib
lib components for the R-DoseFinding package.


%prep
%setup -q -c -n DoseFinding

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530509104

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530509104
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DoseFinding
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DoseFinding
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DoseFinding
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library DoseFinding|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DoseFinding/DESCRIPTION
/usr/lib64/R/library/DoseFinding/INDEX
/usr/lib64/R/library/DoseFinding/Meta/Rd.rds
/usr/lib64/R/library/DoseFinding/Meta/data.rds
/usr/lib64/R/library/DoseFinding/Meta/features.rds
/usr/lib64/R/library/DoseFinding/Meta/hsearch.rds
/usr/lib64/R/library/DoseFinding/Meta/links.rds
/usr/lib64/R/library/DoseFinding/Meta/nsInfo.rds
/usr/lib64/R/library/DoseFinding/Meta/package.rds
/usr/lib64/R/library/DoseFinding/NAMESPACE
/usr/lib64/R/library/DoseFinding/R/DoseFinding
/usr/lib64/R/library/DoseFinding/R/DoseFinding.rdb
/usr/lib64/R/library/DoseFinding/R/DoseFinding.rdx
/usr/lib64/R/library/DoseFinding/data/IBScovars.rda
/usr/lib64/R/library/DoseFinding/data/biom.rda
/usr/lib64/R/library/DoseFinding/data/glycobrom.rda
/usr/lib64/R/library/DoseFinding/data/migraine.rda
/usr/lib64/R/library/DoseFinding/data/neurodeg.rda
/usr/lib64/R/library/DoseFinding/help/AnIndex
/usr/lib64/R/library/DoseFinding/help/DoseFinding.rdb
/usr/lib64/R/library/DoseFinding/help/DoseFinding.rdx
/usr/lib64/R/library/DoseFinding/help/aliases.rds
/usr/lib64/R/library/DoseFinding/help/paths.rds
/usr/lib64/R/library/DoseFinding/html/00Index.html
/usr/lib64/R/library/DoseFinding/html/R.css
/usr/lib64/R/library/DoseFinding/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/DoseFinding/libs/DoseFinding.so
/usr/lib64/R/library/DoseFinding/libs/DoseFinding.so.avx2
/usr/lib64/R/library/DoseFinding/libs/DoseFinding.so.avx512
