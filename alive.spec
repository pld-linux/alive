Summary:	GNU Alive - periodic ping program
Summary(pl.UTF-8):	GNU Alive - program do okresowego pingowania
Name:		alive
Version:	2.0.5
Release:	1
License:	GPL v3+
Group:		Applications/Networking
Source0:	https://ftp.gnu.org/gnu/alive/%{name}-%{version}.tar.lz
# Source0-md5:	c32f7faf1c8a23beadaf7032b151cc24
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/alive/
BuildRequires:	guile-devel
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
Requires:	/bin/ping
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Alive is a keep-alive program for Internet connections. It
repeatedly pings a series of user-specified hosts, thereby encouraging
(one hopes) the involved networks to not disappear.

%description -l pl.UTF-8
GNU Alive to program podtrzymujący połączenia internetowe. Okresowo
pinguje szereg hostów zdefiniowanych przez użytkownika, wspierając
(a przynajmniej dając na to nadzieję), że sieci po drodze nie znikną.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	PING=/bin/ping \
	alive_cv_nice_ping=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/alive
%{_infodir}/alive.info*
