%include	/usr/lib/rpm/macros.perl
Summary:	Data-Compare perl module
Summary(pl):	Modu³ perla Data-Compare
Name:		perl-Data-Compare
Version:	0.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-Compare-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-Compare perl module - compare perl data structures.

%description -l pl
Modu³ perla Data-Compare s³u¿y do porównywania struktur danych.

%prep
%setup -q -n Data-Compare-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Data/Compare.pm
%{_mandir}/man3/*
