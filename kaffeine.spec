Summary:	A KDE xine frontend
Summary(pl):	Frontend do xine pod KDE
Name:		kaffeine
Version:	0.3.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://members.chello.at/kaffeine/download/%{name}-%{version}.tar.gz
# Source0-md5:	92ceceb67a4a672a265c159889e290d0
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-nodoc.patch
URL:		http://members.chello.at/kaffeine/
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.122
BuildRequires:	xine-lib-devel >= 1.0rc0a
Requires:	kdebase-core >= 9:3.1.90
Requires:	xine-lib >= 1.0rc0a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
A powerful, fully integrated with KDE xine GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do xine.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/kaffeine.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%{_datadir}/apps/kaffeine
%{_desktopdir}/kaffeine.desktop
%{_iconsdir}/*/*/apps/kaffeine.png
