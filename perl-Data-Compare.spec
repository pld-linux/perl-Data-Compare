#
# Conditional build:
%bcond_without 	tests		# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Compare
Summary:	Data::Compare perl module
Summary(pl):	Modu³ perla Data::Compare
Name:		perl-Data-Compare
Version:	0.04
Release:	1
# same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ea5828f6c2e42ecff3790a814d4a46c
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.8
%if %{with tests}
BuildRequires:	perl-Scalar-Properties
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Compare perl module - compare perl data structures.

%description -l pl
Modu³ perla Data::Compare s³u¿y do porównywania struktur danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/Compare.pm
%{_mandir}/man3/*
