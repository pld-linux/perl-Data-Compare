#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Compare
Summary:	Data::Compare - compare Perl data structures
Summary(pl):	Data::Compare - porównywanie struktur danych w Perlu
Name:		perl-Data-Compare
Version:	0.11
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abcfeb82c7b8b7490789a03d22f4bc1d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-File-Find-Rule >= 0.11
BuildRequires:	perl-Scalar-Properties
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Compare module compares two Perl data structures recursively.

%description -l pl
Modu³ Data::Compare s³u¿y do rekurencyjnego porównywania dwóch
struktur danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/Compare.pm
%dir %{perl_vendorlib}/Data/Compare
%{perl_vendorlib}/Data/Compare/Plugins
%{_mandir}/man3/*
