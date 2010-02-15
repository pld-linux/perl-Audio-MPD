%bcond_with	tests	# disable "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	MPD
Summary:	Audio::MPD - a Perl module for developing MPD
Summary(pl.UTF-8):	Audio::MPD - moduł Perla do rozwijania aplikacji dla MPD
Name:		perl-Audio-MPD
Version:	1.100430
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JQ/JQUELIN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f40540ccce91c0703ceb0f3659ea86ad
URL:		http://search.cpan.org/dist/Audio-MPD/
%{?with_tests:BuildRequires:	perl-Audio-MPD-Common}
%{?with_tests:BuildRequires:	perl-Class-Accessor}
BuildRequires:	perl-Module-Build >= 1:0.3601
%{?with_tests:BuildRequires:	perl-Test-Pod-Coverage}
%{?with_tests:BuildRequires:	perl-Test-Pod}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio::MPD is a Perl module for developing MPD (Music Player Daemon)
clients and other scripts that control the MPD server.

%description -l pl.UTF-8
Audio::MPD to moduł Perla do rozwijania klientów i innych skryptów
sterujących serwerem MPD (Music Player Daemon).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Audio/MPD.pm
%{perl_vendorlib}/Audio/MPD/*
%{_mandir}/man1/*
%{_mandir}/man3/*
