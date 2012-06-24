#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-BufferText
Summary:	XML::Filter::BufferText Perl module - to guarantee characters in one event
Summary(pl):	Modu� Perla XML::Filter::BufferText - gwarancja przes�ania znak�w w jednym zdarzeniu
Name:		perl-XML-Filter-BufferText
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2992c0387632583b966ab9c965b25512
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.40
BuildRequires:	perl-XML-SAX >= 0.04
BuildRequires:	perl(XML::SAX::Base) >= 1.03
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-SAX >= 0.04
Requires:	perl(XML::SAX::Base) >= 1.03
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple filter. One common cause of grief (and
programmer error) is that XML parsers aren't required to provide
character events in one chunk. They can, but are not forced to, and
most don't. This filter does the trivial but oft-repeated task of
putting all characters into a single event.

%description -l pl
To jest bardzo prosty filtr. Jednym z cz�stych zmartwie� (i b��d�w
programist�w) jest to, �e analizatory XML-a nie musz� dostarcza�
zdarze� znakowych w jednym kawa�ku. Mog�, ale nie s� do tego zmuszone,
i przewa�nie tego nie robi�. Ten filtr wykonuje trywialne, ale cz�sto
wykonywane zadanie umieszczania wszystkich znak�w w jednym zdarzeniu.

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
%doc Changes README
%{perl_vendorlib}/XML/Filter/BufferText.pm
%{_mandir}/man3/*
