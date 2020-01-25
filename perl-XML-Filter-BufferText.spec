#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Filter-BufferText
Summary:	XML::Filter::BufferText Perl module - to guarantee characters in one event
Summary(pl.UTF-8):	Moduł Perla XML::Filter::BufferText - gwarancja przesłania znaków w jednym zdarzeniu
Name:		perl-XML-Filter-BufferText
Version:	1.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2992c0387632583b966ab9c965b25512
URL:		http://search.cpan.org/dist/XML-Filter-BufferText/
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

%description -l pl.UTF-8
To jest bardzo prosty filtr. Jednym z częstych zmartwień (i błędów
programistów) jest to, że analizatory XML-a nie muszą dostarczać
zdarzeń znakowych w jednym kawałku. Mogą, ale nie są do tego zmuszone,
i przeważnie tego nie robią. Ten filtr wykonuje trywialne, ale często
wykonywane zadanie umieszczania wszystkich znaków w jednym zdarzeniu.

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
%{_mandir}/man3/XML::Filter::BufferText.3pm*
