#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-flashClust
Version  : 1.01.2
Release  : 36
URL      : https://cran.r-project.org/src/contrib/flashClust_1.01-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/flashClust_1.01-2.tar.gz
Summary  : Implementation of optimal hierarchical clustering
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-flashClust-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-flashClust package.
Group: Libraries

%description lib
lib components for the R-flashClust package.


%prep
%setup -q -c -n flashClust
cd %{_builddir}/flashClust

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619367347

%install
export SOURCE_DATE_EPOCH=1619367347
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flashClust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flashClust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library flashClust
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc flashClust || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/flashClust/CITATION
/usr/lib64/R/library/flashClust/DESCRIPTION
/usr/lib64/R/library/flashClust/INDEX
/usr/lib64/R/library/flashClust/Meta/Rd.rds
/usr/lib64/R/library/flashClust/Meta/features.rds
/usr/lib64/R/library/flashClust/Meta/hsearch.rds
/usr/lib64/R/library/flashClust/Meta/links.rds
/usr/lib64/R/library/flashClust/Meta/nsInfo.rds
/usr/lib64/R/library/flashClust/Meta/package.rds
/usr/lib64/R/library/flashClust/NAMESPACE
/usr/lib64/R/library/flashClust/R/flashClust
/usr/lib64/R/library/flashClust/R/flashClust.rdb
/usr/lib64/R/library/flashClust/R/flashClust.rdx
/usr/lib64/R/library/flashClust/help/AnIndex
/usr/lib64/R/library/flashClust/help/aliases.rds
/usr/lib64/R/library/flashClust/help/flashClust.rdb
/usr/lib64/R/library/flashClust/help/flashClust.rdx
/usr/lib64/R/library/flashClust/help/paths.rds
/usr/lib64/R/library/flashClust/html/00Index.html
/usr/lib64/R/library/flashClust/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/flashClust/libs/flashClust.so
/usr/lib64/R/library/flashClust/libs/flashClust.so.avx2
