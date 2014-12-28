Summary:	Backup tool
Summary(pl.UTF-8):      Narzędzie do wykonywania kopii zapasowych
Name:		deja-dup
Version:	32.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://launchpad.net/deja-dup/32/32.0/+download/%{name}-%{version}.tar.xz
# Source0-md5:	83e693cfebe397be0c67d3d362ae92c9
URL:		http://launchpad.net/deja-dup
BuildRequires:	cmake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	itstool
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libunique3-devel
BuildRequires:	libxml2-progs
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	perl-Locale-gettext
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vala >= 0.20.0
BuildRequires:	yelp-tools >= 3.2.0
BuildRequires:  libpeas-devel
BuildRequires:  vala-libsecret
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	duplicity >= 0.6.23
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

%description -l pl.UTF-8
Deja Dup jest prostym narzędziem do wykonywania kopii zapasowych. Ukrywa on
złożoność prawidłowych kopii zapasowych (szyfrowanych, poza komputerem i
regularnych) i używa programu duplicity jako mechanizmu.

%package -n nautilus-extension-deja-dup
Summary:	deja-dup extension for Nautilus
Summary(pl.UTF-8):      Rozszerzenie deja-dup dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 3.0.0

%description -n nautilus-extension-deja-dup
This package provides a Nautilus extension that adds the 'Revert to
Previous Version' option to the right-click context menu in Nautilus.

%description -n nautilus-extension-deja-dup -l pl.UTF-8
Ten pakiet dostarcza rozszerzenie Nautilusa dodające opcję "Przywróć do
poprzedniej wersji" do menu kontekstowego uaktywnianego prawym klawiszem myszy
w Nautilusie.

%prep
%setup -q

%build
%cmake \
 -DENABLE_NAUTILUS=ON \
 -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
 -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for lang in az bo en_CA hi io kk ps shn; do
  %{__rm} -rf $RPM_BUILD_ROOT%{_localedir}/$lang
done

for lang in bs en_AU eo my sk; do
  %{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/help/$lang
done

for lang in az be bn bo en_CA fr_CA fy gd hi io kk km mhr my pa se shn si ta ug uz; do
  %{__rm} -rf $RPM_BUILD_ROOT%{_mandir}/$lang
done

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/deja-dup
%attr(755,root,root) %{_bindir}/deja-dup-preferences
%dir %{_libdir}/deja-dup
%dir %{_libdir}/deja-dup/tools
%attr(755,root,root) %{_libdir}/deja-dup/deja-dup-monitor
%{_datadir}/GConf/gsettings/deja-dup.convert
%{_datadir}/deja-dup
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_desktopdir}/deja-dup.desktop
%{_desktopdir}/deja-dup-preferences.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_sysconfdir}/xdg/autostart/deja-dup-monitor.desktop
%{_libdir}/deja-dup/libdeja.so
%{_libdir}/deja-dup/libwidgets.so
%{_libdir}/deja-dup/tools/duplicity.plugin
%{_libdir}/deja-dup/tools/libduplicity.so
%{_datadir}/appdata/deja-dup.appdata.xml
%{_mandir}/man1/*.1*
%lang(ar) %{_mandir}/ar/man1/*.1*
%lang(ast) %{_mandir}/ast/man1/*.1*
%lang(bg) %{_mandir}/bg/man1/*.1*
%lang(bs) %{_mandir}/bs/man1/*.1*
%lang(ca) %{_mandir}/ca/man1/*.1*
%lang(ca@valencia) %{_mandir}/ca@valencia/man1/*.1*
%lang(cs) %{_mandir}/cs/man1/*.1*
%lang(cy) %{_mandir}/cy/man1/*.1*
%lang(da) %{_mandir}/da/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(el) %{_mandir}/el/man1/*.1*
%lang(en_AU) %{_mandir}/en_AU/man1/*.1*
%lang(en_GB) %{_mandir}/en_GB/man1/*.1*
%lang(eo) %{_mandir}/eo/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(et) %{_mandir}/et/man1/*.1*
%lang(eu) %{_mandir}/eu/man1/*.1*
%lang(fa) %{_mandir}/fa/man1/*.1*
%lang(fi) %{_mandir}/fi/man1/*.1*
%lang(fo) %{_mandir}/fo/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(gl) %{_mandir}/gl/man1/*.1*
%lang(he) %{_mandir}/he/man1/*.1*
%lang(hr) %{_mandir}/hr/man1/*.1*
%lang(hu) %{_mandir}/hu/man1/*.1*
%lang(id) %{_mandir}/id/man1/*.1*
%lang(it) %{_mandir}/it/man1/*.1*
%lang(ja) %{_mandir}/ja/man1/*.1*
%lang(ko) %{_mandir}/ko/man1/*.1*
%lang(ku) %{_mandir}/ku/man1/*.1*
%lang(lt) %{_mandir}/lt/man1/*.1*
%lang(lv) %{_mandir}/lv/man1/*.1*
%lang(ml) %{_mandir}/ml/man1/*.1*
%lang(ms) %{_mandir}/ms/man1/*.1*
%lang(nb) %{_mandir}/nb/man1/*.1*
%lang(nl) %{_mandir}/nl/man1/*.1*
%lang(nn) %{_mandir}/nn/man1/*.1*
%lang(oc) %{_mandir}/oc/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%lang(ps) %{_mandir}/ps/man1/*.1*
%lang(pt) %{_mandir}/pt/man1/*.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*.1*
%lang(ro) %{_mandir}/ro/man1/*.1*
%lang(ru) %{_mandir}/ru/man1/*.1*
%lang(sk) %{_mandir}/sk/man1/*.1*
%lang(sl) %{_mandir}/sl/man1/*.1*
%lang(sq) %{_mandir}/sq/man1/*.1*
%lang(sr) %{_mandir}/sr/man1/*.1*
%lang(sv) %{_mandir}/sv/man1/*.1*
%lang(te) %{_mandir}/te/man1/*.1*
%lang(th) %{_mandir}/th/man1/*.1*
%lang(tr) %{_mandir}/tr/man1/*.1*
%lang(uk) %{_mandir}/uk/man1/*.1*
%lang(vi) %{_mandir}/vi/man1/*.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*.1*
%lang(zh_HK) %{_mandir}/zh_HK/man1/*.1*
%lang(zh_TW) %{_mandir}/zh_TW/man1/*.1*

%files -n nautilus-extension-deja-dup
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libdeja-dup.so
