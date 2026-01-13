#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Pipely
Summary:	IO::Pipely - Portably create pipe() or pipe-like handles, one way or another.
Name:		perl-IO-Pipely
Version:	0.006
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64d52842eaba12175a968ab36d846bd5
URL:		https://metacpan.org/release/IO-Pipely/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pipes are troublesome beasts because there are a few different,
incompatible ways to create them.  Not all platforms support all ways,
and some platforms may have hidden difficulties like incomplete or
buggy support.

IO::Pipely provides a couple functions to portably create one- and
two-way pipes and pipe-like socket pairs.  It acknowledges and works
around known platform issues so you don't have to.

On the other hand, it doesn't work around unknown issues, so please
report any problems early and often.

IO::Pipely currently understands pipe(), UNIX-domain socketpair() and
regular IPv4 localhost sockets.  This covers every platform tested so
far, but it's hardly complete.  Please help support other mechanisms,
such as INET-domain socketpair() and IPv6 localhost sockets.

IO::Pipely will use different kinds of pipes or sockets depending on
the operating system's capabilities and the number of directions
requested.  The autodetection may be overridden by specifying a
particular pipe type.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/IO/*.pm
%{_mandir}/man3/*
