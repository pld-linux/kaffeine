
%define		_rc	beta1

Summary:	A KDE xine frontend
Summary(pl):	Frontend do xine pod KDE
Name:		kaffeine
Version:	0.4
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	5f8093e226803f2920d85a7fa30b19fe
Patch0:		%{name}-nodoc.patch
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.122
BuildRequires:	xine-lib-devel >= 1:1.0
Requires:	kdebase-core >= 9:3.1.90
Requires:	xine-lib >= 1:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE xine GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do xine.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_docdir}/kde/HTML

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/%{name}.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;AudioVideo;" \
	>> $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%{_libdir}/kaffeine_part.la
%attr(755,root,root) %{_libdir}/kaffeine_part.so
%{_datadir}/apps/kaffeine
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_desktopdir}/kaffeine.desktop
%{_iconsdir}/*/*/apps/kaffeine.png
