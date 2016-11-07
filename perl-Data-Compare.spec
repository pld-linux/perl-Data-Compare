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
# fill to four decimal digits to avoid epoch bumps after 1.2102
%define	ver	1.25
Version:	%{ver}00
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{ver}.tar.gz
# Source0-md5:	6a397ab5833237f3ca05ed7277b19a7a
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
%setup -q -n %{pdir}-%{pnam}-%{ver}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Data/Compare/Plugins.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/Compare.pm
%dir %{perl_vendorlib}/Data/Compare
%{perl_vendorlib}/Data/Compare/Plugins
%{_mandir}/man3/Data::Compare.3pm*
%{_mandir}/man3/Data::Compare::Plugins*.3pm*
