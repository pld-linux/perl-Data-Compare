%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Compare
Summary:	Data::Compare perl module
Summary(pl):	Modu³ perla Data::Compare
Name:		perl-Data-Compare
Version:	0.02
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Compare perl module - compare perl data structures.

%description -l pl
Modu³ perla Data::Compare s³u¿y do porównywania struktur danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
