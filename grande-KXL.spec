Summary:	grande, a video-oriented game
Summary(pl):	grande - gra video
Name:		grande-KXL
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www2.mwnet.or.jp/~fc3srx7/download/%{name}-%{version}.tar.gz
URL:		http://www2.mwnet.or.jp/~fc3srx7/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	KXL-devel >= 1.1.4
Requires:	KXL >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2D horizon scroll shooting game.

%description -l pl
Strzelanka 2D z poziomym przewijaniem.

%prep
%setup -q

%build
rm -f missing
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
%attr(664,root,games) %config(noreplace) %verify(not md5 size mtime) /var/games/grande.scores
