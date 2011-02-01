Summary:	Backup tool
Name:		deja-dup
Version:	16.1.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://launchpad.net/deja-dup/16/16.1.1/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	debf223cbc8df395ca028a9afaa62c19
URL:		http://launchpad.net/deja-dup
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-progs
BuildRequires:	nautilus-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vala >= 0.10.0
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	duplicity
Requires:	glib2 >= 1:2.26.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deja Dup is a simple backup tool. It hides the complexity of doing
backups the 'right way' (encrypted, off-site, and regular) and uses
duplicity as the backend.

Features:
- Support for local or remote backup locations, including Amazon S3
- Securely encrypts and compresses your data
- Incrementally backs up, letting you restore from any particular
  backup
- Schedules regular backups
- Integrates well into your GNOME desktop

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.{a,la}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install deja-dup.schemas

%preun
%gconf_schema_uninstall deja-dup.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/deja-dup
%attr(755,root,root) %{_bindir}/deja-dup-preferences
%dir %{_libdir}/deja-dup
%attr(755,root,root) %{_libdir}/deja-dup/deja-dup-monitor
%{_desktopdir}/deja-dup.desktop
%{_desktopdir}/deja-dup-preferences.desktop
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_sysconfdir}/xdg/autostart/deja-dup-monitor.desktop
%{_sysconfdir}/gconf/schemas/deja-dup.schemas
%{_mandir}/man1/*.1*
%lang(ar) %{_mandir}/ar/man1/*.1*
%lang(bg) %{_mandir}/bg/man1/*.1*
%lang(cs) %{_mandir}/cs/man1/*.1*
%lang(da) %{_mandir}/da/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(en_GB) %{_mandir}/en_GB/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(fi) %{_mandir}/fi/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(gl) %{_mandir}/gl/man1/*.1*
%lang(he) %{_mandir}/he/man1/*.1*
%lang(hu) %{_mandir}/hu/man1/*.1*
%lang(id) %{_mandir}/id/man1/*.1*
%lang(it) %{_mandir}/it/man1/*.1*
%lang(ja) %{_mandir}/ja/man1/*.1*
%lang(lt) %{_mandir}/lt/man1/*.1*
%lang(nl) %{_mandir}/nb/man1/*.1*
%lang(nl) %{_mandir}/nl/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*.1*
%lang(ps) %{_mandir}/ps/man1/*.1*
%lang(ru) %{_mandir}/ru/man1/*.1*
%lang(sv) %{_mandir}/sv/man1/*.1*
%lang(th) %{_mandir}/th/man1/*.1*
%lang(tr) %{_mandir}/tr/man1/*.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/*.1*
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-deja-dup.so
