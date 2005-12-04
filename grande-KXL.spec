Summary:	grande, a video-oriented game
Summary(pl):	grande - gra video
Name:		grande-KXL
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://kxl.hn.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	a080baa2a154cd90e5da913206606c89
URL:		http://kxl.hn.org/games.php
BuildRequires:	KXL-devel >= 1.1.5
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	KXL >= 1.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2D scroll shooting game.

%description -l pl
Strzelanka 2D z pionowym przewijaniem.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--prefix=%{_datadir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/games

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(2755,root,games) %{_bindir}/grande
%{_datadir}/games/grande
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/grande.scores
