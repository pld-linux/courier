Summary:	Courier mail server
Summary(pl):	Serwer poczty Courier
Name:		courier
Version:	0.35.1
Release:	2
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	http://ftp1.sourceforge.net/courier/%{name}-%{version}.tar.gz
Patch0:		%{name}-openssl-path.patch
URL:		http://www.courier-mta.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
BuildRequires:	db3-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-tools-perl
Provides:	smtpdaemon
#AutoProv:	no
Prereq:		/sbin/chkconfig

%define		apachedir	/home/httpd
%define		_prefix		/usr/lib/courier
%define		_localstatedir	/var/spool/courier
%define		_sysconfdir	/etc/courier
%define		initdir		/etc/rc.d/init.d

# Change the following if your DocumentRoot and cgibindir differ.  This is
# the default redhat build:

%define		_cgibindir		%{apachedir}/cgi-bin
%define		_documentrootdir	%{apachedir}/html
%define		_imageurl		/webmail/

%description
Courier is a fully functional mail server, that can completely take
over the mail services normally provided by sendmail, Qmail, or any
other mail server. Although Courier does not support all legacy
features of existing mail servers, the number of obsoleted functions
is very small, and there are better, and more robust, alternatives
available.

Courier implements many SMTP extensions: DSN, PIPELINING, 8BITMIME.
Courier also implements several new SMTP extensions for mailing list
management and spam filtering.

%description -l pl
Courier jest w pe³ni funkcjonalnym serwerem poczty, mo¿e ca³kowicie
zast±piæ us³ugi pocztowe dawane przez sendmail, Qmaila i inne serwery.
Wprawdzie Courier nie ma wszystkich mo¿liwo¶ci istniej±cych serwerów,
ilo¶æ nie obs³ugiwanych funkcji jesgt bardzo ma³a, i s± dostêpne
lepsze alternatywy.

Courier zawiera wiele rozszerzeñ SMTP: DSN, PIPELINING, 8BITMIME. Ma
tak¿e nowe rozszerzenia SMTP dla pocztowych list dyskusyjnych i
filtrowania spamu.

%package sendmail-wrapper
Summary:	Courier soft links for sendmail
Summary(pl):	Wrapper sendmail do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}

%description sendmail-wrapper
This package contains two soft links from /usr/sbin/sendmail and
/usr/lib/sendmail to %{_bindir}/sendmail. This allows application that
use sendmail to transparently use Courier for sending mail.

%description sendmail-wrapper -l pl
# acc. FHS these symlinks should be in main package...
Ten pakiet zawiera symlinki z /usr/sbin/sendmail i /usr/lib/sendmail
do %{_bindir}/sendmail. Pozwala to aplikacjom u¿ywaj±cym sendmaila
korzystaæ z Couriera.

%package pop3d
Summary:	Courier Integrated POP3 server
Summary(pl):	Zintegrowany serwer POP3 do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}

%description pop3d
This package installs Courier mail server's integrated POP3 server,
which allows you to download mail from your mailbox using any POP3
client. Courier's POP3 server can only be used to download mail from
maildir mailboxes. This server does not support mailbox files. If you
do not need the ability to download your mail using a POP3 client, you
do not need to install this package.

%description pop3d -l pl
Ten pakiet zawiera zintegrowany serwer POP3 do Couriera, pozwalaj±cy
na ¶ci±ganie poczty ze skrzynki przy pomocy dowolnego klienta POP3.
Serwer POP3 Couriera mo¿e byæ u¿ywany tylko ze skrzynkami Maildir, nie
obs³uguje skrzynek w postaci pojedynczych plików.

%package imapd
Summary:	Courier Integrated IMAP server
Summary(pl):	Zintegrowany serwer IMAP do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}
Obsoletes:	courier-imap
Obsoletes:	courier-imap-common

%description imapd
This package installs Courier mail server's integrated IMAP server. If
you do not need the ability to download your mail using an IMAP mail
client, you do not need to install this package. Courier's IMAP server
can only be used to download mail from maildir mailboxes. This server
does not support mailbox files.

This package requires that Courier must be already installed, this is
NOT the standalone version of the Courier-IMAP server, and you cannot
install both this package, and the standalone version of Courier-IMAP.
If you have the standalone version of the Courier-IMAP server already
installed, installing this package will automatically remove the
standalone version.

%description imapd -l pl
Ten pakiet zawiera zintegrowany serwer IMAP do Couriera. Pozwala
¶ci±gaæ pocztê przy pomocy klienta IMAP. Serwer IMAP Couriera mo¿e byæ
u¿ywany tylko ze skrzynami Maildir, nie obs³uguje skrzynek w postaci
pojedynczych plików.

Ten pakiet wymaga serwera Courier, to NIE jest samodzielna wersja
serwera Courier-IMAP. Nie mo¿na te¿ instalowaæ jednocze¶nie tego
pakietu i samodzielnej wersji Courier-IMAP. Zainstalowanie tego
pakietu automatycznie odinstaluje Courier-IMAP je¶li by³ zinstalowany.

%package webmail
Summary:	Courier Integrated HTTP (webmail) server
Summary(pl):	Zintegrowany serwer poczty przez HTTP (webmail) do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}
Requires:	%{_cgibindir}
Requires:	%{_documentrootdir}

%description webmail
This package installs Courier mail server's integrated HTTP webmail
server. If you do not need the ability to access your mail using a web
browser, you do not need to install this package. Courier's webmail
server can only be used to download mail from maildir mailboxes. This
server does not support mailbox files.

This is the same server that's distributed separately under the name
of SqWebMail, however its configuration is customized for the Courier
mail server.

%description webmail -l pl
Ten pakiet zawiera zintegrowany serwer poczty przez HTTP (webmail) dla
Couriera, pozwalaj±cy na dostêp do poczty za pomoc± przegl±darki WWW.
Serwer webmail Couriera mo¿e byæ u¿ywany tylko ze skrzynkami Maildir,
nie obs³uguje skrzynek w postaci pojedynczych plików.

Jest to ten sam serwer, co dystrybuowany oddzielnie pod nazw±
SqWebMail, ale jego konfiguracja jest dostosowana do serwera Courier.

%package mlm
Summary:	Courier Integrated Mailing List Manager
Summary(pl):	Zintegrowany menad¿er list dyskusyjnych do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}

%description mlm
This package installs couriermlm - a mailing list manager for the
Courier mail server. If you do not need the ability to manage mailing
lists, you do not need to install this package.

couriermlm is used to set up, maintain, and run a mailing list.
couriermlm automatically processes subscription and unsubscription
requests, and removes undeliverable addresses from the subscription
rolls. Mailing lists managed by couriermlm require zero human
administrative oversight. couriermlm supports digests, write-only
posting aliases, and moderated mailing lists.

%description mlm -l pl
Ten pakiet zawiera couriermlm - menad¿er list dyskusyjnych dla
Couriera. couriermlm jest u¿ywany do skonfigurowania, zarz±dzania i
prowadzenia pocztowej listy dyskusyjnej. Automatycznie obs³uguje
¿±dania zapisywania i wypisywania i usuwa niedzia³aj±ce adresy z listy
subskrybentów. Listy obs³ugiwane przez couriermlm nie wymagaj± pracy
administratora. couriermlm obs³uguje digesty, aliasy pocztowe tylko do
wysy³ania i listy moderowane.

%package maildrop
Summary:	Courier Integrated mail filter
Summary(pl):	Zintegrowany filtr poczty do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}

%description maildrop
This package installs Courier mail server's integrated mail filter.
You need to install this package if you want to be able to filter your
incoming mail.

%description maildrop -l pl
Ten pakiet zawiera zintegrowany filtr poczty dla Couriera. Jest
potrzebny do filtrowania przychodz±cej poczty.

%package maildrop-wrapper
Summary:	Courier soft links for maildrop
Summary(pl):	Wrapper maildrop do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name}-maildrop = %{version}

%description maildrop-wrapper
This package installs several soft links from the /usr/local/bin
directory to Courier's integrated maildrop mail filter. Maildrop is
available as a standalone package, which installs in %{_bindir}. If
you have applications that expect to find maildrop in /usr/local/bin
you can install this package to create soft links that point to
Courier's integrated maildrop version instead, in order to continue to
use those applications, without needing to reconfigure them.

%description maildrop-wrapper -l pl
# hmmm ??? to be removed...
Ten pakiet zawiera symlinki z katalogu /usr/local/bin do filtru
maildrop Couriera. maildrop jest dostêpnym w oddzielnym pakiecie,
instaluj±cym siê w %{_bindir}. Przydaje siê aplikacjom szukaj±cym
maildropa w /usr/local/bin do u¿ywania z Courierem bez
rekonfigurowania.

%package smtpauth
Summary:	Courier mail server authenticated ESMTP module
Summary(pl):	Modu³ autentykacji ESMTP (SMTP AUTH) do Couriera
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Requires:	%{name} = %{version}

%description smtpauth
Authenticated ESMTP allows remote users to authenticate themselves and
be able to relay outbound mail through the Courier mail server.

%description smtpauth -l pl
SMTP AUTH pozwala zdalnym u¿ytkownikom na autentykacjê i umo¿liwienie
przekazania wychodz±cej poczty poprzez serwer poczty Courier.

%prep
%setup -q
%patch -p1

(cd rootcerts ; autoconf)
%configure2_13 \
	--localstatedir=%{_localstatedir} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--enable-imageurl=%{_imageurl} \
	--with-db=db

%build
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT
umask 022
install -d $RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT/etc/pam.d

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_sysconfdir}/pop3d.authpam $RPM_BUILD_ROOT/etc/pam.d/pop3
ln -sf %{_sysconfdir}/esmtp.authpam $RPM_BUILD_ROOT/etc/pam.d/esmtp
ln -sf %{_sysconfdir}/imapd.authpam $RPM_BUILD_ROOT/etc/pam.d/imap
ln -sf %{_sysconfdir}/webmail.authpam $RPM_BUILD_ROOT/etc/pam.d/webmail

%{__make} install-perms

#
# We're going to create some more config files later, so let's just make
# sure they're processed as all other Courier config files
#

echo '/etc/pam.d/esmtp 644 root root' >>permissions.dat
echo '/etc/profile.d/courier.sh 755 bin bin config' >>permissions.dat
echo '/etc/profile.d/courier.csh 755 bin bin config' >>permissions.dat
echo '%{initdir}/courier 755 bin bin config' >>permissions.dat

#
#  Translate permissions.dat to spec file filelist.
#

perl -e '
$buildroot=$ENV{"RPM_BUILD_ROOT"};
$prefix="%{_prefix}";
$exec_prefix="%{_exec_prefix}";

while (<>)
{
	chop if /\n$/;
	($file,$mode,$uid,$gid,$special)=split(/ +/);
	$file=$prefix if $file eq "$prefix/.";

	next if $special eq "doc";
	next if $file eq "$prefix/doc";

	# Ignore dir/. entries

	next if $file =~ /\/\.$/;

	# Ignore man directories

	next if $file eq "%{_mandir}";
	next if substr($file, 0, length("%{_mandir}")) eq "%{_mandir}"
		&& substr($file, length("%{_mandir}")) =~ /^\/man[1-9]$/;

	$mode = "-" if $special eq "%doc";
	$special="%config" if $special eq "config";
	$special="%dir" if ! -l "$buildroot/$file" && -d "$buildroot/$file";
	if ($special eq "man")
	{
		if ( -l "$buildroot/$file" )
		{
			print STDERR "ln -s " . readlink("$buildroot$file")
				. ".gz $buildroot/$file.gz\n";
			symlink readlink("$buildroot$file")
				. ".gz", "$buildroot/$file.gz";
		}
		else
		{
			print STDERR "gzip <$buildroot$file >$buildroot$file.gz\n";
			system("gzip <$buildroot$file >$buildroot$file.gz ; rm -f $buildroot$file");
		}
		$file="$file.gz"
	}
	$special="" unless $special =~ /%/;

	$special="%attr($mode, $uid, $gid) $special";
	print "$special $file\n";
}

' <permissions.dat >filelist1 || exit 1

sed -n '/imap[\.a-z0-9]*$/p;/imapd-ssl/p' <filelist1 >filelist.imap
sed -n '/pop3[\.a-z0-9]*$/p' <filelist1 >filelist.pop3
sed -n '/couriermlm/p' <filelist1 >filelist.mlm
sed -n '/authstart$/p;/authend$/p' <filelist1 >filelist.auth
sed -n '/maildrop[^/]*$/p;/reformail[^/]*$/p;/reformime[^/]*$/p' <filelist1 >filelist.maildrop
sed '/imap[\.a-z0-9]*$/d;/imapd-ssl/d;/pop3[\.a-z0-9]*$/d;/couriermlm/d;/webmail/d;/ldapaddressbook$/d;/maildrop[^/]*$/d;/reformail[^/]*$/d;/reformime[^/]*$/d;/authstart$/d;/authend$/d' <filelist1 >filelist

sed -n '/sqwebmail/p;/webmail.authpam/p;/webmail-logincache/p;/ldapaddressbook$/p' <filelist1 | sed '/images/d' >filelist.webmail

# Note that we delete all 'webmail's, but copy over only 'sqwebmail's.
# This removes all webmail-related stuff from the main filelist,
# and adds everything except the executable, webmail, to filelist.webmail.
# Here's why:

install -d $RPM_BUILD_ROOT%{_cgibindir}
cp -f $RPM_BUILD_ROOT%{_libexecdir}/courier/webmail/webmail \
	$RPM_BUILD_ROOT%{_cgibindir}/webmail

# And here's why we delete all images from filelist.webmail:

install -d $RPM_BUILD_ROOT%{_documentrootdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/sqwebmail/images $RPM_BUILD_ROOT%{_documentrootdir}/webmail

# Do we need to install a cron job to clean out webmail's cache?

if test -f webmail/cron.cmd
then
	install -d $RPM_BUILD_ROOT/etc/cron.hourly
	cp webmail/cron.cmd $RPM_BUILD_ROOT/etc/cron.hourly/courier-webmail-cleancache
	echo "%attr(555, root, wheel) /etc/cron.hourly/courier-webmail-cleancache" >>filelist.webmail
fi

#
# Move .html documentation back to build dir, so that RPM will move it to
# the appropriate docdir
#

rm -rf htmldoc
mkdir htmldoc
cp -f $RPM_BUILD_ROOT%{_datadir}/htmldoc/* htmldoc
chmod a-w htmldoc/*

# Manually set POP3DSTART and IMAPDSTART to yes, they'll go into a separate
# package, so after it's installed they should be runnable.

sed 's/^POP3DSTART.*/POP3DSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/pop3d >$RPM_BUILD_ROOT%{_sysconfdir}/pop3d.new
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/pop3d.new $RPM_BUILD_ROOT%{_sysconfdir}/pop3d

sed 's/^IMAPDSTART.*/IMAPDSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/imapd >$RPM_BUILD_ROOT%{_sysconfdir}/imapd.new
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/imapd.new $RPM_BUILD_ROOT%{_sysconfdir}/imapd

sed 's/^IMAPDSSLSTART.*/IMAPDSSLSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/imapd-ssl >$RPM_BUILD_ROOT%{_sysconfdir}/imapd.new-ssl
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/imapd.new-ssl $RPM_BUILD_ROOT%{_sysconfdir}/imapd-ssl

#
# Red Hat init.d file
#

install -d $RPM_BUILD_ROOT%{initdir}

cp -f courier.sysvinit $RPM_BUILD_ROOT%{initdir}/courier

#
# Red Hat /etc/profile.d scripts
#

install -d $RPM_BUILD_ROOT/etc/profile.d
cat >$RPM_BUILD_ROOT/etc/profile.d/courier.sh <<EOF
if echo "\$PATH" | tr ':' '\012' | fgrep -qx %{_bindir}
then
	:
else
	if test -w /etc
	then
		PATH="%{_sbindir}:\$PATH"
	fi
	PATH="%{_bindir}:\$PATH"
	export PATH
fi
EOF

cat >$RPM_BUILD_ROOT/etc/profile.d/courier.csh <<EOF

echo "\$PATH" | tr ':' '\012' | fgrep -qx %{_bindir}

if ( \$? ) then
	true
else
	test -w /etc
	if ( \$? ) then
	then
		setenv PATH "%{_sbindir}:\$PATH"
	endif
	setenv PATH "%{_bindir}:\$PATH"
endif
EOF

#
# sendmail soft links
#

install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/lib
install -d $RPM_BUILD_ROOT/usr/bin

ln -sf %{_bindir}/sendmail $RPM_BUILD_ROOT/usr/sbin/sendmail
ln -sf %{_bindir}/sendmail $RPM_BUILD_ROOT/usr/lib/sendmail
ln -sf %{_bindir}/sendmail $RPM_BUILD_ROOT/usr/bin/sendmail

#
# maildrop wrapper soft links
#

install -d $RPM_BUILD_ROOT/usr/local/bin

for f in dotlock maildirmake maildrop makedat reformail reformime deliverquota
do
	ln -s %{_bindir}/$f $RPM_BUILD_ROOT/usr/local/bin/$f
done

for f in makeuserdb pw2userdb userdb userdbpw vchkpw2userdb
do
	ln -s %{_sbindir}/$f $RPM_BUILD_ROOT/usr/local/bin/$f
done

#
# The following directories are not created by default, but I want them here.
#

install -d $RPM_BUILD_ROOT%{_sysconfdir}/userdb
install -d $RPM_BUILD_ROOT%{_localstatedir}/tmp/broken

. courier/uidgid || exit 1

mailuser=daemon
mailgroup=daemon

echo "%attr(700, $mailuser, $mailgroup) %dir %{_sysconfdir}/userdb" >>filelist
echo "%attr(755, $mailuser, $mailgroup) %dir %{_localstatedir}/tmp/broken" >>filelist

gzip -9nf AUTHORS BENCHMARKS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add courier
%{_sbindir}/makealiases 2>/dev/null || true
%{_sbindir}/makesmtpaccess 2>/dev/null || true

# If we do not have a certificate, make one up.

if test ! -f %{_datadir}/esmtpd.pem
then
	%{_sbindir}/mkesmtpdcert
fi

%preun
%{initdir}/courier stop
if test "$1" = "0"
then
        /sbin/chkconfig --del courier
fi

%post imapd
# If we do not have a certificate, make one up.

if test ! -f %{_datadir}/imapd.pem
then
	%{_sbindir}/mkimapdcert
fi
%preun imapd
%{_sbindir}/imapd stop
%{_sbindir}/imapd-ssl stop

%preun pop3d
%{_sbindir}/pop3d stop

%post smtpauth
%{_sbindir}/esmtpd stop
%{_sbindir}/esmtpd start

%postun smtpauth
%{_sbindir}/esmtpd stop
%{_sbindir}/esmtpd start

%files -f filelist
%defattr(644,root,root,755)
%doc *.gz htmldoc/*

%files sendmail-wrapper
%defattr(644,root,root,755)
%attr(-, bin, bin) /usr/sbin/sendmail
%attr(-, bin, bin) /usr/bin/sendmail
%attr(-, bin, bin) /usr/lib/sendmail

%files maildrop-wrapper
%defattr(644,root,root,755)

%attr(-, bin, bin) /usr/local/bin/*

%files pop3d -f filelist.pop3
%defattr(644,root,root,755)
%attr(644, root, wheel) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/pop3

%files imapd -f filelist.imap
%defattr(644,root,root,755)
%attr(644, root, wheel) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/imap

%files webmail -f filelist.webmail
%defattr(644,root,root,755)
%attr(4511, root, wheel) %{_cgibindir}/webmail
%attr(644, root, wheel) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/webmail
%attr(755, bin, bin) %dir %{_documentrootdir}/webmail
%attr(444, bin, bin) %{_documentrootdir}/webmail/*

%files maildrop -f filelist.maildrop
%defattr(644,root,root,755)

%files mlm -f filelist.mlm
%defattr(644,root,root,755)

%files smtpauth -f filelist.auth
%defattr(644,root,root,755)
