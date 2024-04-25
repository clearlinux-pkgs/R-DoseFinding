#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-DoseFinding
Version  : 1.1.1
Release  : 49
URL      : https://cran.r-project.org/src/contrib/DoseFinding_1.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DoseFinding_1.1-1.tar.gz
Summary  : Planning and Analyzing Dose Finding Experiments
Group    : Development/Tools
License  : GPL-3.0
Requires: R-DoseFinding-lib = %{version}-%{release}
Requires: R-ggplot2
Requires: R-mvtnorm
BuildRequires : R-ggplot2
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
of dose-finding experiments (with focus on pharmaceutical Phase

%package lib
Summary: lib components for the R-DoseFinding package.
Group: Libraries

%description lib
lib components for the R-DoseFinding package.


%prep
%setup -q -n DoseFinding
pushd ..
cp -a DoseFinding buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698937441

%install
export SOURCE_DATE_EPOCH=1698937441
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/DoseFinding/Meta/vignette.rds
/usr/lib64/R/library/DoseFinding/NAMESPACE
/usr/lib64/R/library/DoseFinding/R/DoseFinding
/usr/lib64/R/library/DoseFinding/R/DoseFinding.rdb
/usr/lib64/R/library/DoseFinding/R/DoseFinding.rdx
/usr/lib64/R/library/DoseFinding/data/IBScovars.rda
/usr/lib64/R/library/DoseFinding/data/biom.rda
/usr/lib64/R/library/DoseFinding/data/glycobrom.rda
/usr/lib64/R/library/DoseFinding/data/migraine.rda
/usr/lib64/R/library/DoseFinding/data/neurodeg.rda
/usr/lib64/R/library/DoseFinding/doc/analysis_normal.R
/usr/lib64/R/library/DoseFinding/doc/analysis_normal.Rmd
/usr/lib64/R/library/DoseFinding/doc/analysis_normal.html
/usr/lib64/R/library/DoseFinding/doc/binary_data.R
/usr/lib64/R/library/DoseFinding/doc/binary_data.Rmd
/usr/lib64/R/library/DoseFinding/doc/binary_data.html
/usr/lib64/R/library/DoseFinding/doc/faq.R
/usr/lib64/R/library/DoseFinding/doc/faq.Rmd
/usr/lib64/R/library/DoseFinding/doc/faq.html
/usr/lib64/R/library/DoseFinding/doc/index.html
/usr/lib64/R/library/DoseFinding/doc/mult_regimen.R
/usr/lib64/R/library/DoseFinding/doc/mult_regimen.Rmd
/usr/lib64/R/library/DoseFinding/doc/mult_regimen.html
/usr/lib64/R/library/DoseFinding/doc/overview.R
/usr/lib64/R/library/DoseFinding/doc/overview.Rmd
/usr/lib64/R/library/DoseFinding/doc/overview.html
/usr/lib64/R/library/DoseFinding/doc/sample_size.R
/usr/lib64/R/library/DoseFinding/doc/sample_size.Rmd
/usr/lib64/R/library/DoseFinding/doc/sample_size.html
/usr/lib64/R/library/DoseFinding/help/AnIndex
/usr/lib64/R/library/DoseFinding/help/DoseFinding.rdb
/usr/lib64/R/library/DoseFinding/help/DoseFinding.rdx
/usr/lib64/R/library/DoseFinding/help/aliases.rds
/usr/lib64/R/library/DoseFinding/help/paths.rds
/usr/lib64/R/library/DoseFinding/html/00Index.html
/usr/lib64/R/library/DoseFinding/html/R.css
/usr/lib64/R/library/DoseFinding/tests/testgFit.R
/usr/lib64/R/library/DoseFinding/tests/testplanMod.R
/usr/lib64/R/library/DoseFinding/tests/testsDesign.R
/usr/lib64/R/library/DoseFinding/tests/testsFitting.R
/usr/lib64/R/library/DoseFinding/tests/testsMCPMod.R
/usr/lib64/R/library/DoseFinding/tests/testsMCT.R
/usr/lib64/R/library/DoseFinding/tests/testsoptContr.R
/usr/lib64/R/library/DoseFinding/tests/testsplotDRMod.R
/usr/lib64/R/library/DoseFinding/tests/testssampSize.R
/usr/lib64/R/library/DoseFinding/tests/testssamplMod.R
/usr/lib64/R/library/DoseFinding/tests/testthat.R
/usr/lib64/R/library/DoseFinding/tests/testthat/generate_test_datasets.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-MCTtest.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-bMCTtest.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-drmodels.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-fitMod.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-guesst.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-optContr.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-optDesign.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-planMod.R
/usr/lib64/R/library/DoseFinding/tests/testthat/test-powMCTBinCount.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/DoseFinding/libs/DoseFinding.so
/usr/lib64/R/library/DoseFinding/libs/DoseFinding.so.avx2
/usr/lib64/R/library/DoseFinding/libs/DoseFinding.so.avx512
