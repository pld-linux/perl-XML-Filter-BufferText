#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-BufferText
Summary:	XML::Filter::BufferText Perl module - to guarantee characters in one event
Summary(pl):	Modu³ Perla XML::Filter::BufferText - gwarantuj±cy znaki w jednym zdarzeniu
Name:		perl-XML-Filter-BufferText
Version:	1.00
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%{!?_without_tests:BuildRequires:	perl-Test-Simple >= 0.40}
%{!?_without_tests:BuildRequires:	perl-XML-SAX >= 0.04}
%{!?_without_tests:BuildRequires:	perl(XML::SAX::Base) >= 1.03}
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
To jest bardzo prosty filtr. Jednym z czêstych zmartwieñ (i b³êdów
programistów) jest to, ¿e parsery XML nie musz± dostarczaæ zdarzeñ
znakowych w jednym kawa³ku. Mog±, ale nie s± do tego zmuszone, i
przewa¿nie tego nie robi±. Ten filtr wykonuje trywialne, ale czêsto
wykonywane zadanie umieszczania wszystkich znaków w jednym zdarzeniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/XML/Filter/BufferText.pm
%{_mandir}/man3/*
