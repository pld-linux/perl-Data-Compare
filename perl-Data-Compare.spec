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
# Source0-md5:	785f5c49529a8053642b5eb9c49107f7
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/Compare.pm
%{_mandir}/man3/*
