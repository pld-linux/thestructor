Summary:	Simple DocBook Viewer
Summary(pl):	Prosta przegl±darka DocBooka
Name:		thestructor
Version:	0.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake >= 1.5-8
#BuildRequires:	bonobo-devel
#BuildRequires:	gal-devel >= 0.5
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gnome-vfs-devel
BuildRequires:	gtk+-devel >= 1.2.7
#BuildRequires:	libglade-devel
BuildRequires:	libtool
#BuildRequires:	libltdl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Simple DocBook Viewer.

%description -l pl
Prosta przegl±darka DocBooka.

%prep
%setup -q

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
