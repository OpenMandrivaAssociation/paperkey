Summary:	An OpenPGP key archiver
Name:		paperkey
Version:	1.6
Release:	1
License:	GPL-2.0-or-later
URL:		https://www.jabberwocky.com/software/paperkey/
Source0:	https://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gnupg2

%description
A reasonable way to achieve a long term backup of OpenPGP (PGP, GnuPG,
etc) keys is to print them out on paper.  Paper and ink have amazingly
long retention qualities - far longer than the magnetic or optical
means that are generally used to back up computer data.  A paper
backup isn't a replacement for the usual machine readable (tape, CD-R,
DVD-R, etc) backups, but rather as an if-all-else-fails method of
restoring a key.

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build


%install
%make_install

%check
%make_build check

