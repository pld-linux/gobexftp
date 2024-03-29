Summary:	Access devices via ObexFTP e.g. Siemens Mobile Equipment
Summary(pl.UTF-8):	Dostęp poprzez ObexFTP do urządzeń, np. do Siemens Mobile Equipment
Name:		gobexftp
Version:	0.2
Release:	0.1
License:	GPL
Group:		Utilities/Console
Source0:	http://triq.net/obexftp/%{name}-%{version}.tar.gz
# Source0-md5:	5c7ea2b28171eeb06a6a6f6eee2a69e7
Patch0:		%{name}-fix.patch
URL:		http://triq.net/gsm.html
BuildRequires:	libuuid-devel
BuildRequires:	obexftp-devel > 0.10.7-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a GTK+ client for ObexFTP.

%description -l pl.UTF-8
Ten pakiet zawiera klienta GTK+ dla ObexFTP.

%prep
%setup -q
cd src
%patch0 -p1

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS COPYING ChangeLog NEWS README
#%{_bindir}/*
#%{_datadir}/gobexftp/pixmaps/*
