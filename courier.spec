#
# Conditional build:
%bcond_with	fam		# with fam support
#
Summary:	Courier mail server
Summary(pl):	Serwer poczty Courier
Name:		courier
Version:	0.45.5
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	59f69d851740a11a0172eb803f9ab12f
Patch0: 	%{name}-openssl-path.patch
Patch1:		%{name}-withoutfam.patch
Patch2:		%{name}-maildir.patch
Patch3:		%{name}-sendmail_dir.patch
Patch4:		%{name}-start_scripts.patch
Patch5:		%{name}-fix_build.patch
Patch6:		%{name}-certs.patch
URL:		http://www.courier-mta.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	expect
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mailcap
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	openssl-tools >= 0.9.7d
BuildRequires:	openssl-tools-perl >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	perl-devel
BuildRequires:	postgresql-devel
BuildRequires:	sysconftool
BuildRequires:	zlib-devel
%{?with_fam:BuildRequires:	fam-devel}
Requires(post,preun):	/sbin/chkconfig
Requires(post):	openssl-tools >= 0.9.7d
%{?with_fam:Requires:	fam}
Provides:	smtpdaemon
Obsoletes:	exim
Obsoletes:	masqmail
Obsoletes:	nullmailer
Obsoletes:	omta
Obsoletes:	postfix
Obsoletes:	qmail
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	smtpdaemon
Obsoletes:	ssmtp
Obsoletes:	zmailer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apachedir	/home/services/httpd
%define		_datadir	%{_prefix}/share/courier
%define		_mandir		/usr/share/man
%define		_libdir		%{_prefix}/%{_lib}/courier
%define		_libexecdir	%{_libdir}
%define		_localstatedir	/var/spool/courier
%define		_sysconfdir	/etc/courier
%define		_certsdir	%{_sysconfdir}/certs
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
ilo¶æ nie obs³ugiwanych funkcji jest bardzo ma³a, i s± dostêpne
lepsze alternatywy.

Courier zawiera wiele rozszerzeñ SMTP: DSN, PIPELINING, 8BITMIME. Ma
tak¿e nowe rozszerzenia SMTP dla pocztowych list dyskusyjnych i
filtrowania spamu.

%package pop3d
Summary:	Courier Integrated POP3 server
Summary(pl):	Zintegrowany serwer POP3 do Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires(post):	openssl-tools >= 0.9.7d

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
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires(post):	openssl-tools >= 0.9.7d
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

%package webadmin
Summary:	Courier Integrated HTTP administraton panel
Summary(pl):	Panel administracyjny przez HTTP dla Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	%{_cgibindir}
Requires:	webserver

%description webadmin
This is a web-based administration tool. Webadmin is a web CGI
application.

%description webadmin -l pl
Webadmin jest narzêdziem administracyjnym obs³ugiwanym przez WWW.

%package webmail
Summary:	Courier Integrated HTTP (webmail) server
Summary(pl):	Zintegrowany serwer poczty przez HTTP (webmail) do Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
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

%package maildir-tools
Summary:	Tools for mail folders in Maildir format
Summary(pl):	Narzêdzia do zarz±dzania skrzynkami Maildir
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description maildir-tools
This package contains tools for mail folders in Maildir format.

%description maildir-tools -l pl
Ten pakiet zawiera narzêdzia do zarz±dzania folderami w formacie Maildir.

%package mlm
Summary:	Courier Integrated Mailing List Manager
Summary(pl):	Zintegrowany zarz±dca list dyskusyjnych do Couriera
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

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
Ten pakiet zawiera couriermlm - program do zarz±dzania listami
dyskusyjnymi dla Couriera. couriermlm jest u¿ywany do konfigurowania,
zarz±dzania i prowadzenia pocztowej listy dyskusyjnej. Automatycznie
obs³uguje ¿±dania zapisywania i wypisywania oraz usuwa z listy
niedzia³aj±ce adresy subskrybentów. Listy obs³ugiwane przez couriermlm
nie wymagaj± pracy administratora. couriermlm obs³uguje digesty,
aliasy pocztowe tylko do wysy³ania i listy moderowane.

%package maildrop
Summary:	Courier Integrated mail filter
Summary(pl):	Zintegrowany filtr poczty do Couriera
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description maildrop
This package installs Courier mail server's integrated mail filter.
You need to install this package if you want to be able to filter your
incoming mail.

%description maildrop -l pl
Ten pakiet zawiera zintegrowany filtr poczty dla Couriera. Jest
potrzebny do filtrowania przychodz±cej poczty.

%package smtpauth
Summary:	Courier mail server authenticated ESMTP module
Summary(pl):	Modu³ uwierzytelniania ESMTP (SMTP AUTH) do Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description smtpauth
Authenticated ESMTP allows remote users to authenticate themselves and
be able to relay outbound mail through the Courier mail server.

%description smtpauth -l pl
SMTP AUTH pozwala zdalnym u¿ytkownikom na uwierzytelnianie i
umo¿liwienie przekazania wychodz±cej poczty poprzez serwer poczty
Courier.

%package authldap
Summary:	LDAP authentication daemon for Courier mail server
Summary(pl):	Demon autentykacji LDAP do Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description authldap
This package provides LDAP authentication for Courier.

%description authldap -l pl
Ten pakiet pozwala na korzystanie z autentykacji LDAP w Courierze.

%package authmysql
Summary:	MySQL authentication daemon for Courier mail server
Summary(pl):	Demon autentykacji MySQL do Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description authmysql
This package provides MySQL authentication for Courier.

%description authmysql -l pl
Ten pakiet pozwala na korzystanie z autentykacji MySQL w Courierze.

%package authpgsql
Summary:	PostgreSQL authentication daemon for Courier mail server
Summary(pl):	Demon autentykacji PostgreSQL do Couriera
Group:		Networking/Daemons
PreReq:		%{name} = %{version}-%{release}

%description authpgsql
This package provides PostgreSQL authentication for Courier.

%description authpgsql -l pl
Ten pakiet pozwala na korzystanie z autentykacji PostgreSQL w Courierze.

%prep
%setup -q
%patch0 -p1
%{!?with_fam:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
# we don't want fax module
rm -rf courier/module.fax
cp -f /usr/share/automake/config.sub webmail

cd rootcerts
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

cd authlib
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

cd courier
%{__aclocal}
%{__autoconf}
ln -s ../ltmain.sh .
%{__automake}

cd module.esmtp
%{__aclocal}
%{__autoconf}
ln -s ../ltmain.sh .
%{__automake}
cd ../..

cd imap
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

%configure \
	--localstatedir=%{_localstatedir} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--enable-imageurl=%{_imageurl} \
	--with-certsdir=%{_certsdir} \
	--with-db=db \
	--with-mailer=%{_sbindir}/sendmail

%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT
umask 022
install -d -p $RPM_BUILD_ROOT{/etc/{cron.hourly,pam.d},%{initdir}} \
	$RPM_BUILD_ROOT{%{_cgibindir},%{_documentrootdir},%{_prefix}/lib} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{userdb,hosteddomains,shared} \
	$RPM_BUILD_ROOT%{_localstatedir}{/calendar/{private,public},/tmp/broken} \
	$RPM_BUILD_ROOT{/etc/cron.hourly,%{_certsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# fix pam problem
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/*.authpam
for X in imap esmtp pop3 webmail calendar
do
cat > $RPM_BUILD_ROOT/etc/pam.d/$X <<EOF
#%PAM-1.0
auth	required	pam_unix.so shadow nullok
account	required	pam_unix.so
session	required	pam_unix.so
EOF
done

# delete dead links
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/dotforward.1 \
$RPM_BUILD_ROOT%{_mandir}/man1/rmail.1 \
$RPM_BUILD_ROOT%{_mandir}/man7/authcram.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authdaemon.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authdaemond.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authldap.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authmysql.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authpam.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authpwd.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authshadow.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authuserdb.7 \
$RPM_BUILD_ROOT%{_mandir}/man7/authvchkpw.7 \
$RPM_BUILD_ROOT%{_mandir}/man8/esmtpd-msa.8 \
$RPM_BUILD_ROOT%{_mandir}/man8/makesmtpaccess-msa.8 \
$RPM_BUILD_ROOT%{_mandir}/man8/filterctl.8 \
$RPM_BUILD_ROOT%{_mandir}/man8/makeuucpneighbors.8 \
$RPM_BUILD_ROOT%{_mandir}/man8/pw2userdb.8 \
$RPM_BUILD_ROOT%{_mandir}/man8/vchkpw2userdb.8 \
$RPM_BUILD_ROOT%{_mandir}/man8/courierpop3login.8

# make man links
echo '.so dot-forward.1' > $RPM_BUILD_ROOT%{_mandir}/man1/dotforward.1
echo '.so sendmail.1' > $RPM_BUILD_ROOT%{_mandir}/man1/rmail.1
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authcram.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authdaemon.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authdaemond.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authldap.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authmysql.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authpgsql.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authpam.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authpwd.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authshadow.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authuserdb.7
echo '.so authlib.7' > $RPM_BUILD_ROOT%{_mandir}/man7/authvchkpw.7
echo '.so esmtpd.8' > $RPM_BUILD_ROOT%{_mandir}/man8/esmtpd-msa.8
echo '.so courierfilter.8' > $RPM_BUILD_ROOT%{_mandir}/man8/filterctl.8
echo '.so makesmtpaccess.8' > $RPM_BUILD_ROOT%{_mandir}/man8/makesmtpaccess-msa.8
echo '.so courieruucp.8' > $RPM_BUILD_ROOT%{_mandir}/man8/makeuucpneighbors.8
echo '.so makeuserdb.8' > $RPM_BUILD_ROOT%{_mandir}/man8/pw2userdb.8
echo '.so makeuserdb.8' > $RPM_BUILD_ROOT%{_mandir}/man8/vchkpw2userdb.8
echo '.so courierpop3d.8' > $RPM_BUILD_ROOT%{_mandir}/man8/courierpop3login.8

%{__make} install-perms

# Move webmail and webadmin to cgibindir
mv -f $RPM_BUILD_ROOT%{_libexecdir}/courier/webmail/webmail \
	$RPM_BUILD_ROOT%{_cgibindir}/webmail
mv -f $RPM_BUILD_ROOT%{_libexecdir}/courier/webmail/webadmin \
	$RPM_BUILD_ROOT%{_cgibindir}/webadmin

# And here's why we delete all images from filelist.webmail:
mv -f $RPM_BUILD_ROOT%{_datadir}/sqwebmail/images $RPM_BUILD_ROOT%{_documentrootdir}/webmail

# install a cron job to clean out webmail's cache
install webmail/cron.cmd $RPM_BUILD_ROOT/etc/cron.hourly/courier-webmail-cleancache

# Move .html documentation back to build dir, so that RPM will move it to
# the appropriate docdir

rm -rf htmldoc
mkdir htmldoc
mv -f $RPM_BUILD_ROOT%{_datadir}/htmldoc/* htmldoc
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

# Want to have esmtpd running by default
sed 's/^ESMTPDSTART.*/ESMTPDSTART=YES/' <$RPM_BUILD_ROOT%{_sysconfdir}/esmtpd.dist >$RPM_BUILD_ROOT%{_sysconfdir}/esmtpd.new
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/esmtpd.new $RPM_BUILD_ROOT%{_sysconfdir}/esmtpd.dist

# run script from install-configure (make config files)
for confdist in `awk ' $5 == "config" && $1 ~ /\.dist$/ { print $1 }' <permissions.dat`
do /usr/bin/perl ././sysconftool $RPM_BUILD_ROOT$confdist
done

# make locals, esmtpacceptmailfor.dir/default
touch $RPM_BUILD_ROOT%{_sysconfdir}/esmtpacceptmailfor.dir/default
touch $RPM_BUILD_ROOT%{_sysconfdir}/locals

# Make password and unsecureok (files for webadmin)
touch $RPM_BUILD_ROOT%{_sysconfdir}/webadmin/password
touch $RPM_BUILD_ROOT%{_sysconfdir}/webadmin/unsecureok

# create file me to put localdomain
touch $RPM_BUILD_ROOT%{_sysconfdir}/me

# create calendarmode
touch $RPM_BUILD_ROOT%{_sysconfdir}/calendarmode

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

# sendmail soft links
ln -sf %{_sbindir}/sendmail $RPM_BUILD_ROOT/usr/lib/sendmail

# fix rmail link
rm -f $RPM_BUILD_ROOT%{_bindir}/rmail
ln -sf %{_sbindir}/sendmail $RPM_BUILD_ROOT%{_bindir}/rmail

# This link by default is missing
ln -sf %{_datadir}/esmtpd-ssl $RPM_BUILD_ROOT%{_sbindir}/esmtpd-ssl

# remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/*.dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/rfcerr*.txt
rm -rf $RPM_BUILD_ROOT%{_datadir}/faxmail
rm -f $RPM_BUILD_ROOT%{_datadir}/courierwebadmin/*fax*

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- courier < 0.45.5
echo
echo Directory with certificates has changed to %{_certsdir}
echo

%post
/sbin/chkconfig --add courier

if [ "$1" = "1" ]; then
/bin/hostname -f >/etc/courier/me
cat <<EOF

Now courier will refuse to accept SMTP messages except to localhost
add hosts to /etc/courier/esmtpacceptmailfor.dir/default
run makeacceptmailfor

Add hosts to /etc/courier/locals you want to accept mail for
run makealiases

Enter user, who should receive mail for root, mailer-daemon and postmaster
into /etc/courier/aliases/system

EOF
fi

if [ -e /var/lock/subsys/courier ]; then
    %{initdir}/courier restart
else
echo
echo Type "%{initdir}/courier start" to start courier
echo
fi

%preun
if [ "$1" = "0" ]; then
    if [ -e /var/lock/subsys/courier ]; then
	%{initdir}/courier stop
    fi
	/sbin/chkconfig --del courier
fi

%post imapd
if [ -e %{_localstatedir}/tmp/imapd.pid ]; then
    %{_sbindir}/imapd stop
    %{_sbindir}/imapd start
fi
else
echo
echo Type "%{_sbindir}/imapd start" to start imapd server
echo
fi
if [ -e %{_localstatedir}/tmp/imapd-ssl.pid ]; then
    %{_sbindir}/imapd-ssl stop
    %{_sbindir}/imapd-ssl start
fi
else
echo
echo Type "%{_sbindir}/imapd-ssl start" to start imapd-ssl server
echo
fi

%preun imapd
if [ "$1" = "0" ]; then
    if [ -e %{_localstatedir}/tmp/imapd.pid ]; then
	%{_sbindir}/imapd stop
    fi
    if [ -e %{_localstatedir}/tmp/imapd-ssl.pid ]; then
	%{_sbindir}/imapd-ssl stop
    fi
fi

%post pop3d
if [ -e %{_localstatedir}/tmp/pop3d.pid ]; then
    %{_sbindir}/pop3d stop
    %{_sbindir}/pop3d start
fi
else
echo
echo Type "%{_sbindir}/pop3d start" to start pop3d server
echo
fi
if [ -e %{_localstatedir}/tmp/pop3d-ssl.pid ]; then
    %{_sbindir}/pop3d-ssl stop
    %{_sbindir}/pop3d-ssl start
fi
else
echo
echo Type "%{_sbindir}/pop3d-ssl start" to start pop3d-ssl server
echo
fi

%preun pop3d
if [ "$1" = "0" ]; then
    if [ -e %{_localstatedir}/tmp/pop3d.pid ]; then
	%{_sbindir}/pop3d stop
    fi
    if [ -e %{_localstatedir}/tmp/pop3d-ssl.pid ]; then
	%{_sbindir}/pop3d-ssl stop
    fi
fi

%post webadmin
if [ "$1" = "1" ]; then
echo
echo Remember to put your webadmin password to %{_sysconfdir}/webadmin/password
echo
fi

%post webmail
if [ "$1" = "1" ]; then
echo
echo If you want to have calendar starting by default then
echo put word net to %{_sysconfdir}/calendarmode
echo
fi
if [ -e %{_localstatedir}/tmp/sqwebmaild.pid ]; then
    %{_sbindir}/webmaild stop
    %{_sbindir}/webmaild start
else
echo
echo Type "%{_sbindir}/webmaild start" to start webmail server
echo
fi

%preun webmail
if [ "$1" = "0" ]; then
    if [ -e %{_localstatedir}/tmp/sqwebmaild.pid ]; then
	%{_sbindir}/webmaild stop
    fi
fi

%post smtpauth
if [ -e %{_localstatedir}/tmp/esmtpd.pid ]; then
    %{_sbindir}/esmtpd stop
    %{_sbindir}/esmtpd start
fi
if [ -e %{_localstatedir}/tmp/esmtpd-ssl.pid ]; then
    %{_sbindir}/esmtpd-ssl stop
    %{_sbindir}/esmtpd-ssl start
fi

if [ "$1" = "1" ]; then
echo
echo Remember to enable auth in esmtp config files
echo
fi

%postun smtpauth
if [ "$1" = "0" ]; then
    if [ -e %{_localstatedir}/tmp/esmtpd.pid ]; then
	%{_sbindir}/esmtpd stop
	%{_sbindir}/esmtpd start
    fi
    if [ -e %{_localstatedir}/tmp/esmtpd-ssl.pid ]; then
	%{_sbindir}/esmtpd-ssl stop
	%{_sbindir}/esmtpd-ssl start
    fi
fi

%post authldap
if ps -A |grep -q authdaemond.lda; then
	%{_libdir}/authlib/authdaemond stop
	%{_libdir}/authlib/authdaemond start
fi

%postun authldap
if [ -x %{_libdir}/authlib/authdaemond ]; then
	if ps -A |grep -q authdaemond.lda; then
		%{_libdir}/authlib/authdaemond stop;
		%{_libdir}/authlib/authdaemond start;
	fi
fi

%post authmysql
if ps -A |grep -q authdaemond.mys; then
	%{_libdir}/authlib/authdaemond stop
	%{_libdir}/authlib/authdaemond start
fi

%postun authmysql
if [ -x %{_libdir}/authlib/authdaemond ]; then
	if ps -A |grep -q authdaemond.mys; then
		%{_libdir}/authlib/authdaemond stop;
		%{_libdir}/authlib/authdaemond start;
	fi
fi

%post authpgsql
if ps -A |grep -q authdaemond.pgs; then
	%{_libdir}/authlib/authdaemond stop
	%{_libdir}/authlib/authdaemond start
fi

%postun authpgsql
if [ -x %{_libdir}/authlib/authdaemond ]; then
	if ps -A |grep -q authdaemond.pgs; then
		%{_libdir}/authlib/authdaemond stop;
		%{_libdir}/authlib/authdaemond start;
	fi
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS BENCHMARKS ChangeLog INSTALL NEWS README TODO htmldoc/[adehqstu]*
%doc htmldoc/courierperl* htmldoc/courier.html htmldoc/courier[fltu]*
%doc htmldoc/local* htmldoc/mailbot* htmldoc/mailq* htmldoc/make*
%doc htmldoc/mime* htmldoc/mkesmtpd* htmldoc/modules* htmldoc/preline*
%{_mandir}/man1/sendmail.1*
%{_mandir}/man1/preline.1*
%{_mandir}/man1/cancelmsg.1*
%{_mandir}/man1/lockmail.1*
%{_mandir}/man1/mailbot.1*
%{_mandir}/man1/makemime.1*
%{_mandir}/man1/mimegpg.1*
%{_mandir}/man1/makedat.1*
%{_mandir}/man1/testmxlookup.1*
%{_mandir}/man1/dot-forward.1*
%{_mandir}/man1/couriertls.1*
%{_mandir}/man1/courierlogger.1*
%{_mandir}/man1/mailq*
%{_mandir}/man1/couriertcpd*
%{_mandir}/man1/dotforward.1*
%{_mandir}/man1/rmail.1*
%{_mandir}/man5/dot-courier.5*
%{_mandir}/man7/localmailfilter.7*
%{_mandir}/man7/authlib.7*
%{_mandir}/man7/authcram.7*
%{_mandir}/man7/authdaemon.7*
%{_mandir}/man7/authdaemond.7*
%{_mandir}/man7/authpam.7*
%{_mandir}/man7/authpwd.7*
%{_mandir}/man7/authshadow.7*
%{_mandir}/man7/authuserdb.7*
%{_mandir}/man7/authvchkpw.7*
%{_mandir}/man8/courierfilter.8*
%{_mandir}/man8/courierperlfilter.8*
%{_mandir}/man8/dupfilter.8*
%{_mandir}/man8/courier.8*
%{_mandir}/man8/courierldapaliasd.8*
%{_mandir}/man8/deliverquota.8*
%{_mandir}/man8/esmtpd.8*
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
%{_mandir}/man8/courieruucp.8*
%{_mandir}/man8/esmtpd-msa.8*
%{_mandir}/man8/filterctl.8*
%{_mandir}/man8/makesmtpaccess-msa.8*
%{_mandir}/man8/makeuucpneighbors.8*
%{_mandir}/man8/pw2userdb.8*
%{_mandir}/man8/vchkpw2userdb.8*
%dir %{_sysconfdir}
%attr(750,daemon,root) %dir %{_certsdir}
%attr(755,daemon,daemon) %dir %{_sysconfdir}/hosteddomains
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/me
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ldapaddressbook
%attr(755,daemon,daemon) %dir %{_sysconfdir}/aliasdir
%attr(750,daemon,daemon) %dir %{_sysconfdir}/aliases
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/enablefiltering
%attr(755,daemon,daemon) %dir %{_sysconfdir}/smtpaccess
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/smtpaccess/default
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/esmtpacceptmailfor.dir/default
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/locals
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/courierd
%attr(640,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/aliases/system
%attr(644,root,root) %{_sysconfdir}/quotawarnmsg.example
%dir %{_libdir}
%dir %{_libdir}/courier
%dir %{_datadir}
%{_datadir}/rootcerts
%attr(755,root,root) %dir %{_datadir}/courierwebadmin
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
%dir %{_libdir}/courier/modules
%dir %{_libdir}/courier/modules/uucp
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/module.uucp
%attr(755,root,root) %{_libdir}/courier/modules/uucp/courieruucp
%attr(755,root,root) %{_sbindir}/makeuucpneighbors
%attr(755,root,root) %{_datadir}/makeuucpneighbors
%dir %{_libdir}/courier/modules/local
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/module.local
%attr(755,root,root) %{_libdir}/courier/modules/local/courierlocal
%attr(755,root,root) %{_libdir}/courier/modules/local/courierdeliver
%attr(755,root,root) %{_bindir}/preline
%dir %{_libdir}/courier/modules/esmtp
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/module.esmtp
%attr(750,root,daemon) %{_libdir}/courier/modules/esmtp/courieresmtp
%attr(750,root,daemon) %{_libdir}/courier/modules/esmtp/courieresmtpd
%attr(755,root,root) %{_libdir}/courier/modules/esmtp/addcr
%attr(755,root,root) %{_sbindir}/courieresmtpd
%attr(755,root,root) %{_bindir}/addcr
%attr(755,root,root) %{_sbindir}/esmtpd
%attr(755,root,root) %{_datadir}/esmtpd
%attr(755,root,root) %{_sbindir}/esmtpd-ssl
%attr(755,root,root) %{_datadir}/esmtpd-ssl
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
%attr(755,root,root) %{_sbindir}/sharedindexinstall
%attr(755,root,root) %{_sbindir}/sharedindexsplit
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/esmtpd
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/esmtpd-msa
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/esmtpd-ssl
%attr(755,daemon,daemon) %dir %{_sysconfdir}/esmtpacceptmailfor.dir
%attr(755,daemon,daemon) %dir %{_sysconfdir}/esmtppercentrelay.dir
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/esmtpd.cnf
%attr(600,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/esmtpauthclient
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsndelayed.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsndelivered.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsnfailed.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsnrelayed.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsnfooter.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsnsubjectnotice.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsnsubjectwarn.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dsnheader.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/module.dsn
%dir %{_libdir}/courier/modules/dsn
%attr(755,root,root) %{_libdir}/courier/modules/dsn/courierdsn
%{_libdir}/courier/modules/modules.ctl
%attr(4550,daemon,daemon) %{_libdir}/courier/submitmkdir
%attr(750,root,daemon) %{_libdir}/courier/courierd
%attr(750,root,daemon) %{_libdir}/courier/aliasexp
%attr(750,root,daemon) %{_libdir}/courier/aliascombine
%attr(750,root,daemon) %{_libdir}/courier/aliascreate
%attr(750,root,daemon) %{_libdir}/courier/submit
%attr(755,root,root) %{_libdir}/courier/makedatprog
%attr(755,root,root) %{_sbindir}/authenumerate
%attr(6555,daemon,daemon) %{_bindir}/cancelmsg
%attr(755,root,root) %{_sbindir}/courier
%attr(755,root,root) %{_datadir}/courierctl.start
%attr(755,root,root) %{_bindir}/couriertls
%attr(755,root,root) %{_sbindir}/couriertcpd
%attr(755,root,root) %{_sbindir}/courierlogger
%attr(755,root,root) %{_bindir}/courier-config
%attr(755,root,root) %{_bindir}/deliverquota
%attr(755,root,root) %{_bindir}/dotforward
%attr(755,root,root) %{_bindir}/lockmail
%attr(755,root,root) %{_bindir}/mailbot
%attr(2755,root,daemon) %{_bindir}/mailq
%attr(750,root,daemon) %{_datadir}/makealiases
%attr(750,root,daemon) %{_sbindir}/makealiases
%attr(755,root,root) %{_datadir}/makedat
%attr(755,root,root) %{_bindir}/makedat
%attr(755,root,root) %{_datadir}/makehosteddomains
%attr(755,root,root) %{_sbindir}/makehosteddomains
%attr(755,root,root) %{_bindir}/makemime
%attr(755,root,root) %{_datadir}/makeuserdb
%attr(755,root,root) %{_sbindir}/makeuserdb
%attr(755,root,root) %{_bindir}/mimegpg
%attr(755,root,root) %{_datadir}/pw2userdb
%attr(755,root,root) %{_sbindir}/pw2userdb
%attr(4755,root,root) %{_bindir}/rmail
%attr(755,root,root) %{_sbindir}/showconfig
%attr(750,root,daemon) %{_sbindir}/showmodules
%attr(4755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) %{_bindir}/testmxlookup
%attr(755,root,root) %{_datadir}/userdb
%attr(755,root,root) %{_sbindir}/userdb
%attr(755,root,root) %{_sbindir}/userdbpw
%attr(755,root,root) %{_datadir}/vchkpw2userdb
%attr(755,root,root) %{_sbindir}/vchkpw2userdb
%attr(640,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ldapaliasrc
%attr(700,daemon,daemon) %{_sbindir}/courierldapaliasd
%attr(660,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authdaemonrc
%dir %{_libdir}/authlib
%attr(755,root,root) %{_libdir}/authlib/authdaemon
%attr(755,root,root) %{_libdir}/authlib/authdaemond.plain
%attr(755,root,root) %{_libdir}/authlib/authdaemond
%attr(770,daemon,daemon) %dir %{_localstatedir}/authdaemon
%attr(755,root,root) %dir %{_libdir}/authlib/changepwd
%attr(4755,root,root) %{_libdir}/authlib/changepwd/authdaemon.passwd
%attr(755,root,root) %{_libdir}/authlib/changepwd/authsystem.passwd
%attr(755,root,root) %{_datadir}/authsystem.passwd
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/esmtp
%attr(755,root,root) /etc/profile.d/courier.sh
%attr(755,root,root) /etc/profile.d/courier.csh
%attr(754,root,root) /etc/rc.d/init.d/courier
%attr(700,daemon,daemon) %dir %{_sysconfdir}/userdb
%attr(750,daemon,daemon) %dir %{_sysconfdir}/shared
%attr(755,daemon,daemon) %dir %{_localstatedir}/tmp/broken
%attr(755,root,root) /usr/lib/sendmail

%files pop3d
%defattr(644,root,root,755)
%doc htmldoc/*pop3d*
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/pop3
%{_mandir}/man8/courierpop3d.8*
%{_mandir}/man8/courierpop3login.8*
%{_mandir}/man8/mkpop3dcert.8*
%{_mandir}/man8/pop3d.8*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-45pop3.pl
%{_datadir}/courierwebadmin/admin-45pop3.html
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pop3d
%attr(600,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pop3d.cnf
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pop3d-ssl
%attr(755,root,root) %{_libdir}/courier/courierpop3d
%attr(755,root,root) %{_libdir}/courier/courierpop3login
%attr(755,root,root) %{_datadir}/mkpop3dcert
%attr(755,root,root) %{_sbindir}/mkpop3dcert
%attr(755,root,root) %{_datadir}/pop3d
%attr(755,root,root) %{_sbindir}/pop3d
%attr(755,root,root) %{_datadir}/pop3d-ssl
%attr(755,root,root) %{_sbindir}/pop3d-ssl

%files imapd
%defattr(644,root,root,755)
%doc htmldoc/*imapd*
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/imap
%{_mandir}/man8/imapd.8*
%{_mandir}/man8/mkimapdcert.8*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-40imap.pl
%attr(644,root,root) %{_datadir}/courierwebadmin/admin-40imap.html
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/imapd
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/imapd-ssl
%attr(600,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/imapd.cnf
%attr(755,root,root) %{_libdir}/courier/imaplogin
%attr(755,root,root) %{_sbindir}/imapd
%attr(755,root,root) %{_sbindir}/imapd-ssl
%attr(755,root,root) %{_datadir}/imapd
%attr(755,root,root) %{_datadir}/imapd-ssl
%attr(755,root,root) %{_bindir}/imapd
%attr(755,root,root) %{_datadir}/mkimapdcert
%attr(755,root,root) %{_sbindir}/mkimapdcert

%files webadmin
%defattr(644,root,root,755)
%attr(4755,root,root) %{_cgibindir}/webadmin
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin/added
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin/removed
%attr(400,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/webadmin/password
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/webadmin/unsecureok
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-main.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-save.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-cancel.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-[0235]*.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-10password.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/dumpenv.pl
%attr(755,root,root) %{_datadir}/courierwebadmin/webadmin.pl
%{_datadir}/courierwebadmin/admin-[0235]*.html
%{_datadir}/courierwebadmin/admin-10password.html
%{_datadir}/courierwebadmin/admin-main.html
%{_datadir}/courierwebadmin/admin-save.html
%{_datadir}/courierwebadmin/login.html
%{_datadir}/courierwebadmin/notsupp.html
%{_datadir}/courierwebadmin/unsecure.html
%{_datadir}/courierwebadmin/webadmin.pm

%files webmail
%defattr(644,root,root,755)
%doc htmldoc/pcp* gpglib/README.html
%attr(4755,root,root) %{_cgibindir}/webmail
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/webmail
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/calendar
%{_documentrootdir}/webmail
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sqwebmaild
%attr(755,root,root) %{_sbindir}/webmaild
%dir %{_datadir}/sqwebmail
%dir %{_datadir}/sqwebmail/html
%dir %{_datadir}/sqwebmail/html/en-us
%{_datadir}/sqwebmail/html/en
%config %{_datadir}/sqwebmail/html/en-us/[CILT]*
%{_datadir}/sqwebmail/html/en-us/*.html
%{_datadir}/sqwebmail/html/en-us/*.txt
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-47webmail.pl
%{_datadir}/courierwebadmin/admin-47webmail.html
%attr(755,root,root) %{_datadir}/sqwebmail/cleancache.pl
%attr(755,root,root) %{_datadir}/sqwebmail/ldapsearch
%attr(755,root,root) %{_datadir}/sqwebmail/sendit.sh
%attr(755,root,root) %{_datadir}/sqwebmail/webgpg
%attr(755,root,root) %{_sbindir}/webgpg
%attr(755,root,root) %{_libdir}/courier/pcpd
%attr(755,root,root) %{_libdir}/courier/sqwebmaild
%attr(700, bin, bin) %dir %{_localstatedir}/webmail-logincache
%attr(755,root,root) /etc/cron.hourly/courier-webmail-cleancache
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/calendarmode
%attr(751,bin,bin) %dir %{_localstatedir}/calendar
%attr(700,bin,bin) %dir %{_localstatedir}/calendar/localcache
%attr(750,bin,bin) %dir %{_localstatedir}/calendar/private
%attr(755,bin,bin) %dir %{_localstatedir}/calendar/public

%files maildrop
%defattr(644,root,root,755)
%doc htmldoc/r* htmldoc/maildrop* htmldoc/lockmail*
%{_mandir}/man1/maildrop.1*
%{_mandir}/man1/refor*
%{_mandir}/man5/maildrop*
%attr(644,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/maildrop
%attr(4755,root,root) %{_bindir}/maildrop
%attr(755,root,root) %{_bindir}/reformail
%attr(755,root,root) %{_bindir}/reformime

%files maildir-tools
%defattr(644,root,root,755)
%doc maildir/README.*.html htmldoc/maildir*
%{_mandir}/man1/maildirmake.1*
%{_mandir}/man1/maildirkw.1*
%{_mandir}/man1/maildiracl.1*
%{_mandir}/man5/maildir.5*
%{_mandir}/man7/maildirquota.7*
%attr(755,root,root) %{_bindir}/maildirmake
%attr(755,root,root) %{_bindir}/maildirkw
%attr(755,root,root) %{_bindir}/maildiracl

%files mlm
%defattr(644,root,root,755)
%doc htmldoc/couriermlm.html
%{_mandir}/man1/couriermlm.1*
%attr(755,root,root) %{_bindir}/couriermlm
%{_datadir}/couriermlm

%files smtpauth
%defattr(644,root,root,755)
%attr(4750,root,daemon) %{_libdir}/courier/modules/esmtp/authstart
%attr(755,root,root) %{_libdir}/courier/modules/esmtp/authend

%files authldap
%defattr(644,root,root,755)
%doc authlib/README.ldap
%attr(755,root,root) %{_libdir}/authlib/authdaemond.ldap
%attr(660,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authldaprc
%{_mandir}/man7/authldap.7*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-15ldap.pl
%{_datadir}/courierwebadmin/admin-15ldap.html
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-15ldapa.pl
%{_datadir}/courierwebadmin/admin-15ldapa.html

%files authmysql
%defattr(644,root,root,755)
%doc authlib/README.authmysql.html authlib/README.authmysql.myownquery
%attr(755,root,root) %{_libdir}/authlib/authdaemond.mysql
%attr(660,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authmysqlrc
%{_mandir}/man7/authmysql.7*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-15mysql.pl
%{_datadir}/courierwebadmin/admin-15mysql.html

%files authpgsql
%defattr(644,root,root,755)
%doc authlib/README.authpostgres.html
%attr(755,root,root) %{_libdir}/authlib/authdaemond.pgsql
%attr(660,daemon,daemon) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/authpgsqlrc
%{_mandir}/man7/authpgsql.7*
%attr(755,root,root) %{_datadir}/courierwebadmin/admin-15pgsql.pl
%{_datadir}/courierwebadmin/admin-15pgsql.html
