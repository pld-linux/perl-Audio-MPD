#
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	MPD
Summary:	Audio::MPD - a Perl module for developing MPD
Summary(pl.UTF-8):	Audio::MPD - moduł perla do rozwijania apikacji dla MPD
Name:		perl-Audio-MPD
Version:	0.18.2
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82e403caee99d0ee5dbe4a0fedf6de6c
URL:		http://search.cpan.org/dist/Audio-MPD/
BuildRequires:	perl-Module-Build
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
%{perl_vendorlib}/Audio/*
%{_mandir}/man1/*
%{_mandir}/man3/*
