# TODO
%define		qtver	5.4
%define		kdever	5.11

Summary:	Full featured Multimedia-Player for KDE
Summary(pl.UTF-8):	W pełni funkcjonalny odtwarzacz multimediów dla KDE
Name:		kaffeine
Version:	2.0.18
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	https://download.kde.org/Attic/kaffeine/%{name}-%{version}.tar.xz
# Source0-md5:	185cd114e1ebcf15b98674e872a53556
URL:		https://apps.kde.org/kaffeine/
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
# libdvbv5
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
Kaffeine is a full featured Multimedia-Player for KDE.

%description -l pl.UTF-8
Kaffeine to w pełni funkcjonalny odtwarzacz multimediów dla KDE.

%prep
%setup -q

%build
install -d build
cd build
%cmake ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

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
%doc Changelog README.md TODO
%attr(755,root,root) %{_bindir}/kaffeine
%dir %{_datadir}/kaffeine
%{_datadir}/kaffeine/scanfile.dvb
%{_datadir}/metainfo/org.kde.kaffeine.appdata.xml
# better owner? no other users so far
%dir %{_datadir}/profiles
%{_datadir}/profiles/kaffeine.profile.xml
%{_datadir}/solid/actions/kaffeine_play_audiocd.desktop
%{_datadir}/solid/actions/kaffeine_play_dvd.desktop
%{_datadir}/solid/actions/kaffeine_play_videocd.desktop
%{_desktopdir}/org.kde.kaffeine.desktop
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
