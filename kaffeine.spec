# TODO
# - kaffeine-mozilla-0.2.tar.bz2 (Starter-Plugin for Mozilla)
# - check: http://kaffeine.sourceforge.net/index.php?page=faq#question4

%bcond_without	gstreamer	# build without gstreamer part

Summary:	A KDE xine frontend
Summary(pl):	Frontend do xine pod KDE
Name:		kaffeine
Version:	0.8.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kaffeine/%{name}-%{version}.tar.bz2
# Source0-md5:	3abba4ff76ffdd109e1f1cfe286e5b5b
Patch0:		%{name}-win32-path.patch
Patch1:		%{name}-desktop.patch
URL:		http://kaffeine.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.122
BuildRequires:	xine-lib-devel >= 1:1.0.2
%if %{with gstreamer}
BuildRequires:	gstreamer-plugins-devel < 0.9.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.4
Requires:	gstreamer < 0.9.0
Requires:	gstreamer >= 0.8.4
%endif
Requires:	kdebase-core >= 9:3.1.90
Requires:	kdelibs >= 9:3.4.0-4
Requires:	libdvdcss
Requires:	xine-lib >= 1:1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE xine GUI.

%description -l pl
W pe�ni zintegrowany z KDE frontend do xine.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--with%{?!with_gstreamer:out}-gstreamer
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# no devel libraries, why did these get installed?
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}
rm $RPM_BUILD_ROOT%{_includedir}/%{name}_export.h

rm $RPM_BUILD_ROOT/%{_datadir}/mimelnk/application/x-mplayer2.desktop

# pick docs
%find_lang %{name} --with-kde
# second try. pic locale files
# FIXME: remove version?
%find_lang %{name}-%{version} --with-kde
cat  %{name}-%{version}.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%attr(755,root,root) %{_libdir}/libkmediapart.so.0.0.1
%{_libdir}/libkmediapart.la
%attr(755,root,root) %{_libdir}/libkaffeineaudioencoder.so.0.0.1
%{_libdir}/libkaffeineaudioencoder.la
%attr(755,root,root) %{_libdir}/kde3/libkaffeinepart.so
%{_libdir}/kde3/libkaffeinepart.la
%{_libdir}/kde3/libkaffeinemp3lame.la
%attr(755,root,root) %{_libdir}/kde3/libkaffeinemp3lame.so
%{_libdir}/kde3/libkaffeineoggvorbis.la
%attr(755,root,root) %{_libdir}/kde3/libkaffeineoggvorbis.so
%{_datadir}/apps/kaffeine
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/services/kaffeine_part.desktop
%{_datadir}/services/kaffeinemp3lame.desktop
%{_datadir}/services/kaffeineoggvorbis.desktop
%{_datadir}/servicetypes/kaffeineaudioencoder.desktop
%{_desktopdir}/kde/kaffeine.desktop
%{_iconsdir}/[!l]*/*/*/*.png
#%{_mandir}/man1/kaffeine.1*
#%lang(de) %{_mandir}/de/man1/kaffeine.1*

# gstreamer part
%if %{with gstreamer}
%attr(755,root,root) %{_libdir}/kde3/libgstreamerpart.so
%{_libdir}/kde3/libgstreamerpart.la
%dir %{_datadir}/apps/gstreamerpart
%{_datadir}/apps/gstreamerpart/gstreamer_part.rc
%{_datadir}/services/gstreamer_part.desktop
%endif
