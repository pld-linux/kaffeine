# TODO
%define		qtver	5.4
%define		kdever	5.11

Summary:	Full featured Multimedia-Player for KDE
Summary(pl.UTF-8):	Frontend do xine pod KDE
Name:		kaffeine
Version:	2.0.10
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://download.kde.org/stable/kaffeine/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	89fd6614379789f594af30bc5c72dd63
Patch0:		%{name}-loglevel.patch
URL:		http://kaffeine.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-kcoreaddons-devel >= %{kdever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kdever}
BuildRequires:	kf5-kdoctools-devel >= %{kdever}
BuildRequires:	kf5-ki18n-devel >= %{kdever}
BuildRequires:	kf5-kio-devel >= %{kdever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kdever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kdever}
BuildRequires:	kf5-kxmlgui-devel >= %{kdever}
BuildRequires:	kf5-solid-devel >= %{kdever}
BuildRequires:	libv4l-devel
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	vlc-devel >= 1.2
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5Network >= %{qtver}
Requires:	Qt5Sql >= %{qtver}
Requires:	Qt5Sql-sqldriver-sqlite3 >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	Qt5X11Extras >= %{qtver}
Requires:	hicolor-icon-theme
Requires:	kf5-kcoreaddons >= %{kdever}
Requires:	kf5-kdbusaddons >= %{kdever}
Requires:	kf5-ki18n >= %{kdever}
Requires:	kf5-kio >= %{kdever}
Requires:	kf5-kwidgetsaddons >= %{kdever}
Requires:	kf5-kwindowsystem >= %{kdever}
Requires:	kf5-kxmlgui >= %{kdever}
Requires:	kf5-solid >= %{kdever}
Requires:	vlc >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaffeine is a full featured Multimedia-Player for KDE. By default it
uses xine as backend.

%description -l pl.UTF-8
W pełni zintegrowany z KDE frontend do xine.

%prep
%setup -q
%patch0 -p0

%build
install -d build
cd build
%cmake ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}

rm -r $RPM_BUILD_ROOT%{_localedir}/{sr@ijekavian,sr@ijekavianlatin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dtvdaemon
%attr(755,root,root) %{_bindir}/kaffeine
%{_datadir}/appdata/org.kde.kaffeine.appdata.xml
%{_desktopdir}/org.kde.kaffeine.desktop
%dir %{_datadir}/kaffeine
%{_datadir}/kaffeine/scanfile.dvb
%{_datadir}/solid/actions/kaffeine_play_audiocd.desktop
%{_datadir}/solid/actions/kaffeine_play_dvd.desktop
%{_datadir}/solid/actions/kaffeine_play_videocd.desktop
%{_iconsdir}/hicolor/scalable/apps/kaffeine.svg
%{_iconsdir}/hicolor/scalable/actions/*.svg
%{_iconsdir}/hicolor/scalable/devices/*.svg
%{_iconsdir}/hicolor/scalable/mimetypes/*.svg
%{_iconsdir}/hicolor/scalable/places/*.svg
%{_iconsdir}/hicolor/scalable/status/*.svg
%{_mandir}/man1/kaffeine.1*
%lang(ca) %{_mandir}/ca/man1/kaffeine.1*
%lang(it) %{_mandir}/it/man1/kaffeine.1*
%lang(nl) %{_mandir}/nl/man1/kaffeine.1*
%lang(pt) %{_mandir}/pt/man1/kaffeine.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kaffeine.1*
%lang(sv) %{_mandir}/sv/man1/kaffeine.1*
%lang(uk) %{_mandir}/uk/man1/kaffeine.1*
