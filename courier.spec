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
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	openssl-tools-perl
BuildRequires:	pam-devel
BuildRequires:	perl-devel
BuildRequires:	zlib-devel
Provides:	smtpdaemon
Prereq:		/sbin/chkconfig

%define		apachedir	/home/httpd
%define		_prefix		/usr/lib/courier
%define		_localstatedir	/var/spool/courier
%define		_sysconfdir	/etc/courier
%define		_mandir		/usr/share/man
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

# install a cron job to clean out webmail's cache

install -d $RPM_BUILD_ROOT/etc/cron.hourly
install webmail/cron.cmd $RPM_BUILD_ROOT/etc/cron.hourly/courier-webmail-cleancache

# Move .html documentation back to build dir, so that RPM will move it to
# the appropriate docdir

rm -rf htmldoc
mkdir htmldoc
cp -f $RPM_BUILD_ROOT%{_datadir}/htmldoc/* htmldoc
chmod a-w htmldoc/*

# Manually set POP3DSTART and IMAPDSTART to yes, they'll go into a separate
# package, so after it's installed they should be runnable.

sed 's/^POP3DSTART.*/POP3DSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/pop3d.dist >$RPM_BUILD_ROOT%{_sysconfdir}/pop3d.new
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/pop3d.new $RPM_BUILD_ROOT%{_sysconfdir}/pop3d.dist

sed 's/^POP3DSSLSTART.*/POP3DSSLSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/pop3d-ssl.dist >$RPM_BUILD_ROOT%{_sysconfdir}/pop3d-ssl.new
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/pop3d-ssl.new $RPM_BUILD_ROOT%{_sysconfdir}/pop3d-ssl.dist

sed 's/^IMAPDSTART.*/IMAPDSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/imapd.dist >$RPM_BUILD_ROOT%{_sysconfdir}/imapd.new
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/imapd.new $RPM_BUILD_ROOT%{_sysconfdir}/imapd.dist

sed 's/^IMAPDSSLSTART.*/IMAPDSSLSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/imapd-ssl.dist >$RPM_BUILD_ROOT%{_sysconfdir}/imapd.new-ssl
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/imapd.new-ssl $RPM_BUILD_ROOT%{_sysconfdir}/imapd-ssl.dist

#
# Red Hat init.d file
#

install -d $RPM_BUILD_ROOT%{initdir}
install courier.sysvinit $RPM_BUILD_ROOT%{initdir}/courier

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

ln -sf %{_bindir}/sendmail $RPM_BUILD_ROOT/usr/sbin/sendmail
ln -sf %{_bindir}/sendmail $RPM_BUILD_ROOT/usr/lib/sendmail

#
# The following directories are not created by default, but I want them here.
#

install -d $RPM_BUILD_ROOT%{_sysconfdir}/userdb
install -d $RPM_BUILD_ROOT%{_localstatedir}/tmp/broken

gzip -9nf AUTHORS BENCHMARKS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add courier
%{_sbindir}/makealiases 2>/dev/null || true
%{_sbindir}/makesmtpaccess 2>/dev/null || true

# If we do not have a certificate, make one up.
if [ ! -f %{_datadir}/esmtpd.pem ]; then
	%{_sbindir}/mkesmtpdcert
fi

%preun
if [ "$1" = "0" ]; then
	%{initdir}/courier stop
        /sbin/chkconfig --del courier
fi

%post imapd
# If we do not have a certificate, make one up.
if [ ! -f %{_datadir}/imapd.pem ]; then
	%{_sbindir}/mkimapdcert
fi
%{_sbindir}/imapd stop
%{_sbindir}/imapd start
%{_sbindir}/imapd-ssl stop
%{_sbindir}/imapd-ssl start

%preun imapd
if [ "$1" = "0" ]; then
	%{_sbindir}/imapd stop
	%{_sbindir}/imapd-ssl stop
fi

%post pop3d
%{_sbindir}/pop3d stop
%{_sbindir}/pop3d start

%preun pop3d
if [ "$1" = "0" ]; then
	%{_sbindir}/pop3d stop
fi

%post smtpauth
%{_sbindir}/esmtpd stop
%{_sbindir}/esmtpd start

%postun smtpauth
if [ "$1" = "0" ]; then
	%{_sbindir}/esmtpd stop
	%{_sbindir}/esmtpd start
fi

%files
%defattr(644,root,root,755)
%doc *.gz htmldoc/*
%{_mandir}/man1/sendmail.1*
%{_mandir}/man1/preline.1*
%{_mandir}/man1/maildirmake.1*
%{_mandir}/man1/cancelmsg.1*
%{_mandir}/man1/dotlock.1*
%{_mandir}/man1/mailbot.1*
%{_mandir}/man1/makemime.1*
%{_mandir}/man1/mimegpg.1*
%{_mandir}/man1/makedat.1*
%{_mandir}/man1/testmxlookup.1*
%{_mandir}/man1/dot-forward.1*
%{_mandir}/man1/couriertls.1*
%{_mandir}/man1/rmail.1*
%{_mandir}/man1/dotforward.1*
%{_mandir}/man5/dot-courier.5*
%{_mandir}/man7/localmailfilter.7*
%{_mandir}/man7/maildirquota.7*
%{_mandir}/man8/auth*
%{_mandir}/man8/courierfilter.8*
%{_mandir}/man8/courierperlfilter.8*
%{_mandir}/man8/dupfilter.8*
%{_mandir}/man8/filterctl.8*
%{_mandir}/man8/courier.8*
%{_mandir}/man8/courierldapaliasd.8*
%{_mandir}/man8/couriertcpd.8*
%{_mandir}/man8/deliverquota.8*
%{_mandir}/man8/esmtpd.8*
%{_mandir}/man8/mailq.8*
%{_mandir}/man8/makeacceptmailfor.8*
%{_mandir}/man8/makehosteddomains.8*
%{_mandir}/man8/mkesmtpdcert.8*
%{_mandir}/man8/makealiases.8*
%{_mandir}/man8/makepercentrelay.8*
%{_mandir}/man8/makesmtpaccess.8*
%{_mandir}/man8/makeuserdb.8*
%{_mandir}/man8/submit.8*
%{_mandir}/man8/userdb.8*
%{_mandir}/man8/userdbpw.8*
%{_mandir}/man8/pw2userdb.8*
%{_mandir}/man8/vchkpw2userdb.8*
%{_mandir}/man8/makesmtpaccess-msa.8*
%{_mandir}/man8/esmtpd-msa.8*
%{_mandir}/man8/courieruucp.8*
%{_mandir}/man8/makeuucpneighbors.8*
%config %{_sysconfdir}/ldapaddressbook.dist
%dir %{_sysconfdir}
%attr(755,daemon,daemon) %dir %{_sysconfdir}/aliasdir
%attr(750,daemon,daemon) %dir %{_sysconfdir}/aliases
%attr(644,daemon,daemon) %config %{_sysconfdir}/enablefiltering
%attr(755,daemon,daemon) %dir %{_sysconfdir}/smtpaccess
%attr(644,daemon,daemon) %config %{_sysconfdir}/smtpaccess/default
%attr(644,daemon,daemon) %config %{_sysconfdir}/courierd.dist
%attr(640,daemon,daemon) %config %{_sysconfdir}/aliases/system
%attr(644,daemon,daemon) %config %{_sysconfdir}/pop3d-ssl.dist
%attr(644,root,root) %{_sysconfdir}/quotawarnmsg.example
%dir %{_prefix}
%dir %{_bindir}
%dir %{_sbindir}
%dir %{_libdir}
%dir %{_libdir}/courier
%dir %{_datadir}
%{_datadir}/rootcerts
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin/added
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin/removed
%attr(755,root,root) %dir %{_datadir}/courierwebadmin
%attr(755,root,root) %{_datadir}/courierwebadmin/webadmin.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/dumpenv.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-main.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-save.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-cancel.pl
%{_datadir}/courierwebadmin/login.html
%{_datadir}/courierwebadmin/admin-save.html
%{_datadir}/courierwebadmin/admin-main.html
%{_datadir}/courierwebadmin/unsecure.html
%dir %{_libdir}/filters
%attr(755,root,root) %{_libdir}/filters/*
%attr(755,root,root) %{_datadir}/perlfilter-*.pl
%dir %{_localstatedir}
%attr(770,daemon,daemon) %dir %{_localstatedir}/tmp
%attr(750,daemon,daemon) %dir %{_localstatedir}/msgs
%attr(750,daemon,daemon) %dir %{_localstatedir}/msgq
%attr(750,daemon,daemon) %dir %{_localstatedir}/filters
%attr(750,daemon,daemon) %dir %{_localstatedir}/allfilters
%attr(750,daemon,daemon) %dir %{_sysconfdir}/filters
%attr(750,daemon,daemon) %dir %{_sysconfdir}/filters/active
%attr(754,root,daemon) %{_datadir}/filterctl
%attr(754,root,daemon) %{_sbindir}/filterctl
%attr(754,root,daemon) %{_sbindir}/courierfilter
%dir %{_datadir}/htmldoc
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-[0123]*.pl
%{_datadir}/courierwebadmin/admin-[0123]*.html
%{_datadir}/courierwebadmin/webadmin.pm
%{_datadir}/courierwebadmin/notsupp.html
%dir %{_libdir}/courier/modules
%dir %{_libdir}/courier/modules/uucp
%attr(644,daemon,daemon) %config %{_sysconfdir}/module.uucp
%attr(755,root,root) %{_libdir}/courier/modules/uucp/courieruucp
%attr(755,root,root) %{_sbindir}/makeuucpneighbors
%attr(755,root,root) %{_datadir}/makeuucpneighbors
%dir %{_libdir}/courier/modules/local
%attr(644,daemon,daemon) %config %{_sysconfdir}/module.local
%attr(644,daemon,daemon) %config %{_sysconfdir}/authmodulelist
%attr(755,root,root) %{_libdir}/courier/modules/local/courierlocal
%attr(755,root,root) %{_libdir}/courier/modules/local/courierdeliver
%attr(755,root,root) %{_bindir}/preline
%dir %{_libdir}/courier/modules/esmtp
%attr(644,daemon,daemon) %config %{_sysconfdir}/module.esmtp
%attr(750,root,daemon) %{_libdir}/courier/modules/esmtp/courieresmtp
%attr(750,root,daemon) %{_libdir}/courier/modules/esmtp/courieresmtpd
%attr(755,root,root) %{_libdir}/courier/modules/esmtp/addcr
%attr(755,root,root) %{_sbindir}/courieresmtpd
%attr(755,root,root) %{_bindir}/addcr
%attr(755,root,root) %{_sbindir}/esmtpd
%attr(755,root,root) %{_datadir}/esmtpd
%attr(755,root,root) %{_sbindir}/makesmtpaccess
%attr(755,root,root) %{_datadir}/makesmtpaccess
%attr(755,root,root) %{_sbindir}/makeacceptmailfor
%attr(755,root,root) %{_datadir}/makeacceptmailfor
%attr(755,root,root) %{_sbindir}/makepercentrelay
%attr(755,root,root) %{_datadir}/makepercentrelay
%attr(755,root,root) %{_sbindir}/mkesmtpdcert
%attr(755,root,root) %{_datadir}/mkesmtpdcert
%attr(755,root,root) %{_sbindir}/esmtpd-msa
%attr(755,root,root) %{_sbindir}/makesmtpaccess-msa
%attr(644,daemon,daemon) %config %{_sysconfdir}/esmtpd.dist
%attr(644,daemon,daemon) %config %{_sysconfdir}/esmtpd-msa.dist
%attr(755,daemon,daemon) %dir %{_sysconfdir}/esmtpacceptmailfor.dir
%attr(755,daemon,daemon) %dir %{_sysconfdir}/esmtppercentrelay.dir
%attr(644,daemon,daemon) %config %{_sysconfdir}/esmtp.authpam
%attr(644,daemon,daemon) %config %{_sysconfdir}/esmtpd.cnf
%attr(600,daemon,daemon) %config %{_sysconfdir}/esmtpauthclient
%dir %{_libdir}/courier/modules/dsn
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsndelayed.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsndelivered.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsnfailed.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsnrelayed.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsnfooter.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsnsubjectnotice.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsnsubjectwarn.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/dsnheader.txt
%attr(644,daemon,daemon) %config %{_sysconfdir}/module.dsn
%attr(755,root,root) %{_libdir}/courier/modules/dsn/courierdsn
%{_libdir}/courier/modules/modules.ctl
%attr(4550,daemon,daemon) %{_libdir}/courier/submitmkdir
%attr(750,root,daemon) %{_libdir}/courier/courierd
%attr(750,root,daemon) %{_libdir}/courier/aliasexp
%attr(750,root,daemon) %{_libdir}/courier/aliascombine
%attr(750,root,daemon) %{_libdir}/courier/aliascreate
%attr(750,root,daemon) %{_libdir}/courier/submit
%attr(755,root,root) %{_libdir}/courier/makedatprog
%attr(755,root,root) %{_sbindir}/courier
%attr(755,root,root) %{_sbindir}/showconfig
%attr(750,root,daemon) %{_sbindir}/showmodules
%attr(755,root,root) %{_sbindir}/userdbpw
%attr(755,root,root) %{_sbindir}/couriertcpd
%attr(755,root,root) %{_sbindir}/logger
%attr(6555,daemon,daemon) %{_bindir}/cancelmsg
%attr(755,root,root) %{_bindir}/courier-config
%attr(2755,root,daemon) %{_bindir}/mailq
%attr(755,root,root) %{_bindir}/maildirmake
%attr(4755,root,root) %{_bindir}/sendmail
%attr(4755,root,root) %{_bindir}/rmail
%attr(755,root,root) %{_bindir}/dotlock
%attr(755,root,root) %{_bindir}/deliverquota
%attr(755,root,root) %{_bindir}/mailbot
%attr(755,root,root) %{_bindir}/makemime
%attr(755,root,root) %{_bindir}/mimegpg
%attr(755,root,root) %{_bindir}/dotforward
%attr(755,root,root) %{_datadir}/makedat
%attr(755,root,root) %{_bindir}/makedat
%attr(755,root,root) %{_bindir}/testmxlookup
%attr(750,root,daemon) %{_datadir}/makealiases
%attr(750,root,daemon) %{_sbindir}/makealiases
%attr(755,root,root) %{_datadir}/makehosteddomains
%attr(755,root,root) %{_sbindir}/makehosteddomains
%attr(755,root,root) %{_datadir}/pop3d-ssl
%attr(755,root,root) %{_sbindir}/pop3d-ssl
%attr(755,root,root) %{_datadir}/makeuserdb
%attr(755,root,root) %{_sbindir}/makeuserdb
%attr(755,root,root) %{_datadir}/webgpg
%attr(755,root,root) %{_sbindir}/webgpg
%attr(755,root,root) %{_datadir}/userdb
%attr(755,root,root) %{_sbindir}/userdb
%attr(755,root,root) %{_datadir}/pw2userdb
%attr(755,root,root) %{_sbindir}/pw2userdb
%attr(755,root,root) %{_datadir}/vchkpw2userdb
%attr(755,root,root) %{_sbindir}/vchkpw2userdb
%attr(755,root,root) %{_datadir}/courierctl.start
%attr(755,root,root) %{_bindir}/couriertls
%attr(640,daemon,daemon) %config %{_sysconfdir}/ldapaliasrc.dist
%attr(700,daemon,daemon) %{_sbindir}/courierldapaliasd
%attr(660,daemon,daemon) %config %{_sysconfdir}/authldaprc.dist
%attr(660,daemon,daemon) %config %{_sysconfdir}/authmysqlrc.dist
%attr(660,daemon,daemon) %config %{_sysconfdir}/authdaemonrc.dist
%dir %{_libdir}/authlib
%attr(755,root,root) %{_libdir}/authlib/authdaemon
%attr(755,root,root) %{_libdir}/authlib/authdaemond.plain
%attr(755,root,root) %{_libdir}/authlib/authdaemond.ldap
%attr(755,root,root) %{_libdir}/authlib/authdaemond.mysql
%attr(755,root,root) %{_libdir}/authlib/authdaemond
%attr(770,daemon,daemon) %dir %{_localstatedir}/authdaemon
%attr(755,root,root) %dir %{_libdir}/authlib/changepwd
%attr(4755,root,root) %{_libdir}/authlib/changepwd/authdaemon.passwd
%attr(755,root,root) %{_libdir}/authlib/changepwd/authsystem.passwd
%attr(755,root,root) %{_datadir}/authsystem.passwd
%config(noreplace) /etc/pam.d/esmtp
%attr(755,root,root) /etc/profile.d/courier.sh
%attr(755,root,root) /etc/profile.d/courier.csh
%attr(754,root,root) /etc/rc.d/init.d/courier
%attr(700,daemon,daemon) %dir %{_sysconfdir}/userdb
%attr(755,daemon,daemon) %dir %{_localstatedir}/tmp/broken
/usr/lib/sendmail
/usr/sbin/sendmail

%files pop3d
%defattr(644,root,root,755)
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/pop3
%{_mandir}/man8/courierpop3login.8*
%{_mandir}/man8/courierpop3d.8*
%{_mandir}/man8/pop3d.8*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-45pop3.pl
%{_datadir}/courierwebadmin/admin-45pop3.html
%attr(644,daemon,daemon) %config %{_sysconfdir}/pop3d.dist
%attr(644,daemon,daemon) %config %{_sysconfdir}/pop3d.authpam
%attr(600,daemon,daemon) %config %{_sysconfdir}/pop3d.cnf
%attr(755,root,root) %{_libdir}/courier/courierpop3d
%attr(755,root,root) %{_libdir}/courier/courierpop3login
%attr(755,root,root) %{_datadir}/pop3d
%attr(755,root,root) %{_sbindir}/pop3d
%attr(755,root,root) %{_datadir}/mkpop3dcert
%attr(755,root,root) %{_sbindir}/mkpop3dcert

%files imapd
%defattr(644,root,root,755)
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/imap
%{_mandir}/man8/imapd.8*
%{_mandir}/man8/mkimapdcert.8*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-40imap.pl
%attr(644,root,root) %{_datadir}/courierwebadmin/admin-40imap.html
%attr(644,daemon,daemon) %config %{_sysconfdir}/imapd.dist
%attr(644,daemon,daemon) %config %{_sysconfdir}/imapd-ssl.dist
%attr(644,daemon,daemon) %config %{_sysconfdir}/imapd.authpam
%attr(600,daemon,daemon) %config %{_sysconfdir}/imapd.cnf
%attr(755,root,root) %{_libdir}/courier/imaplogin
%attr(755,root,root) %{_sbindir}/imapd
%attr(755,root,root) %{_sbindir}/imapd-ssl
%attr(755,root,root) %{_datadir}/imapd
%attr(755,root,root) %{_datadir}/imapd-ssl
%attr(755,root,root) %{_bindir}/imapd
%attr(755,root,root) %{_datadir}/mkimapdcert
%attr(755,root,root) %{_sbindir}/mkimapdcert

%files webmail
%defattr(644,root,root,755)
%attr(4755,root,root) %{_cgibindir}/webmail
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/webmail
%{_documentrootdir}/webmail
%dir %{_datadir}/sqwebmail
%dir %{_datadir}/sqwebmail/html
%dir %{_datadir}/sqwebmail/html/en-us
%{_datadir}/sqwebmail/html/en
%config %{_datadir}/sqwebmail/html/en-us/[CIL]*
%{_datadir}/sqwebmail/html/en-us/*.html
%attr(755,root,root) %{_datadir}/sqwebmail/cleancache.pl
%attr(755,root,root) %{_datadir}/sqwebmail/sendit.sh
%attr(755,root,root) %{_datadir}/sqwebmail/ldapsearch
%attr(700, bin, bin) %dir %{_localstatedir}/webmail-logincache
%attr(644,daemon,daemon) %config /etc/courier/webmail.authpam
%attr(755,root,root) /etc/cron.hourly/courier-webmail-cleancache

%files maildrop
%defattr(644,root,root,755)
%{_mandir}/man1/maildrop.1*
%{_mandir}/man1/refor*
%{_mandir}/man5/maildrop*
%attr(644,daemon,daemon) %config /etc/courier/maildrop
%attr(755,root,root)  %{_bindir}/reformail
%attr(755,root,root)  %{_bindir}/reformime
%attr(4755,root,root) %{_bindir}/maildrop

%files mlm
%defattr(644,root,root,755)
%{_mandir}/man1/couriermlm.1*
%attr(755,root,root) %{_bindir}/couriermlm
%{_datadir}/couriermlm

%files smtpauth
%defattr(644,root,root,755)
%attr(4750,root,daemon) %{_libdir}/courier/modules/esmtp/authstart
%attr(755,root,root) %{_libdir}/courier/modules/esmtp/authend
