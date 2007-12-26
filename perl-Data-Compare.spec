#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	Compare
Summary:	Data::Compare - compare Perl data structures
Summary(pl.UTF-8):	Data::Compare - porównywanie struktur danych w Perlu
Name:		perl-Data-Compare
Version:	0.17
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48cee57d6928937218b4058dc62c666e
URL:		http://search.cpan.org/dist/Data-Compare/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-File-Find-Rule >= 0.11
BuildRequires:	perl-Scalar-Properties
BuildRequires:	perl-perldoc
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Compare module compares two Perl data structures recursively.

%description -l pl.UTF-8
Moduł Data::Compare służy do rekurencyjnego porównywania dwóch
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
