# TODO
# - doesn't -webadmin need webserver integration?
# - use rc-scripts in %%post scriptlets
# - init.d script, pre and post for webmlm?
#
# Conditional build:
%bcond_without	fam		# with fam support
%bcond_with	gnutls		# GnuTLS instead of OpenSSL
%bcond_with	socks		# (Courier) Socks support
%bcond_with	tests		# without tests
#
Summary:	Courier mail server
Summary(pl.UTF-8):	Serwer poczty Courier
Name:		courier
Version:	1.0.9
Release:	4
License:	GPL v3 with OpenSSL exception
Group:		Networking/Daemons
Source0:	http://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	3a716dd3eabadb991ffcc4ee9d06afa0
Patch1:		%{name}-withoutfam.patch
Patch2:		%{name}-maildir.patch
Patch3:		%{name}-sendmail_dir.patch
Patch4:		%{name}-start_scripts.patch
Patch5:		%{name}-certs.patch
Patch6:		%{name}-filterbindir.patch
Patch7:		ac.patch
URL:		http://www.courier-mta.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	courier-authlib-devel >= 0.66
%{?with_socks:BuildRequires:	courier-sox-devel}
BuildRequires:	courier-unicode-devel >= 2.1
BuildRequires:	db-devel
BuildRequires:	expect
%{?with_fam:BuildRequires:	fam-devel}
BuildRequires:	gettext-tools
# or gnupg2 when --with-gpg2
BuildRequires:	gnupg
%{?with_gnutls:BuildRequires:	gnutls-devel >= 3.0}
%{?with_gnutls:BuildRequires:	libgcrypt-devel}
%{?with_gnutls:BuildRequires:	libgpg-error-devel}
BuildRequires:	libidn-devel >= 0.0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mailcap
BuildRequires:	openldap-devel >= 2.3.0
%{!?with_gnutls:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	openssl-tools >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel >= 5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	sysconftool
Requires(post,preun):	/sbin/chkconfig
# even if using OpenSSL libraries, Courier uses certtool from GnuTLS
Requires:	/usr/bin/certtool
Requires:	courier-authlib >= 0.66
Requires:	courier-unicode >= 2.1
Requires:	rc-scripts
Provides:	smtpdaemon
Obsoletes:	smtpdaemon
Conflicts:	cone < 1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/spool/courier
%define		_sysconfdir	/etc/courier
%define		_certsdir	%{_sysconfdir}/certs

%define		_webapps	/etc/webapps
%define		_cgibindir	/usr/lib/cgi-bin
%define		_imagedir	%{_datadir}/courier/sqwebmail/images
%define		_imageurl	/webmail

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

%description -l pl.UTF-8
Courier jest w pełni funkcjonalnym serwerem poczty, może całkowicie
zastąpić usługi pocztowe dawane przez sendmail, Qmaila i inne serwery.
Wprawdzie Courier nie ma wszystkich możliwości istniejących serwerów,
ilość nie obsługiwanych funkcji jest bardzo mała, i są dostępne lepsze
alternatywy.

Courier zawiera wiele rozszerzeń SMTP: DSN, PIPELINING, 8BITMIME. Ma
także nowe rozszerzenia SMTP dla pocztowych list dyskusyjnych i
filtrowania spamu.

%package pop3d
Summary:	Courier Integrated POP3 server
Summary(pl.UTF-8):	Zintegrowany serwer POP3 do Couriera
Group:		Networking/Daemons/POP3
Requires(post):	openssl-tools >= 0.9.7d
Requires:	%{name} = %{version}-%{release}
Provides:	pop3daemon
Obsoletes:	pop3daemon

%description pop3d
This package installs Courier mail server's integrated POP3 server,
which allows you to download mail from your mailbox using any POP3
client. Courier's POP3 server can only be used to download mail from
maildir mailboxes. This server does not support mailbox files. If you
do not need the ability to download your mail using a POP3 client, you
do not need to install this package.

%description pop3d -l pl.UTF-8
Ten pakiet zawiera zintegrowany serwer POP3 do Couriera, pozwalający
na ściąganie poczty ze skrzynki przy pomocy dowolnego klienta POP3.
Serwer POP3 Couriera może być używany tylko ze skrzynkami Maildir, nie
obsługuje skrzynek w postaci pojedynczych plików.

%package imapd
Summary:	Courier Integrated IMAP server
Summary(pl.UTF-8):	Zintegrowany serwer IMAP do Couriera
Group:		Networking/Daemons
Requires(post):	openssl-tools >= 0.9.7d
Requires:	%{name} = %{version}-%{release}
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

%description imapd -l pl.UTF-8
Ten pakiet zawiera zintegrowany serwer IMAP do Couriera. Pozwala
ściągać pocztę przy pomocy klienta IMAP. Serwer IMAP Couriera może być
używany tylko ze skrzynkami Maildir, nie obsługuje skrzynek w postaci
pojedynczych plików.

Ten pakiet wymaga serwera Courier, to NIE jest samodzielna wersja
serwera Courier-IMAP. Nie można też instalować jednocześnie tego
pakietu i samodzielnej wersji Courier-IMAP. Zainstalowanie tego
pakietu automatycznie odinstaluje Courier-IMAP jeśli był zinstalowany.

%package webadmin
Summary:	Courier Integrated HTTP administraton panel
Summary(pl.UTF-8):	Panel administracyjny przez HTTP dla Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	filesystem >= 3.0-11
Requires:	webapps
Requires:	webserver = apache
Conflicts:	apache-base < 2.2.0-8
Conflicts:	apache1 < 1.3.34-5.11

%description webadmin
This is a web-based administration tool. Webadmin is a web CGI
application.

%description webadmin -l pl.UTF-8
Webadmin jest narzędziem administracyjnym obsługiwanym przez WWW.

%package webmail
Summary:	Courier Integrated HTTP (webmail) server
Summary(pl.UTF-8):	Zintegrowany serwer poczty przez HTTP (webmail) do Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	filesystem >= 3.0-11
Requires:	webapps
Requires:	webserver = apache
Conflicts:	apache-base < 2.2.0-8
Conflicts:	apache1 < 1.3.34-5.11

%description webmail
This package installs Courier mail server's integrated HTTP webmail
server. If you do not need the ability to access your mail using a web
browser, you do not need to install this package. Courier's webmail
server can only be used to download mail from maildir mailboxes. This
server does not support mailbox files.

This is the same server that's distributed separately under the name
of SqWebMail, however its configuration is customized for the Courier
mail server.

%description webmail -l pl.UTF-8
Ten pakiet zawiera zintegrowany serwer poczty przez HTTP (webmail) dla
Couriera, pozwalający na dostęp do poczty za pomocą przeglądarki WWW.
Serwer webmail Couriera może być używany tylko ze skrzynkami Maildir,
nie obsługuje skrzynek w postaci pojedynczych plików.

Jest to ten sam serwer, co dystrybuowany oddzielnie pod nazwą
SqWebMail, ale jego konfiguracja jest dostosowana do serwera Courier.

%package webmlm
Summary:	Courier web-based access to some couriermlm commands
Summary(pl.UTF-8):	Dostęp WWW do niektórych poleceń couriermlm do Couriera
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Requires:	filesystem >= 3.0-11
Requires:	webapps
Requires:	webserver = apache
Conflicts:	apache-base < 2.2.0-8
Conflicts:	apache1 < 1.3.34-5.11

%description webmlm
WebMLM is a service that offers an alternative web-based access to
some couriermlm commands, as an alternative to submitting them via
E-mail.

%description webmlm -l pl.UTF-8
WebMLM to serwis oferujący dostęp WWW do wybranych poleceń couriermlm
jako alternatywę do wysyłania ich poprzez e-mail.

%package maildir-tools
Summary:	Tools for mail folders in Maildir format
Summary(pl.UTF-8):	Narzędzia do zarządzania skrzynkami Maildir
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description maildir-tools
This package contains tools for mail folders in Maildir format.

%description maildir-tools -l pl.UTF-8
Ten pakiet zawiera narzędzia do zarządzania folderami w formacie
Maildir.

%package mlm
Summary:	Courier Integrated Mailing List Manager
Summary(pl.UTF-8):	Zintegrowany zarządca list dyskusyjnych do Couriera
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

%description mlm -l pl.UTF-8
Ten pakiet zawiera couriermlm - program do zarządzania listami
dyskusyjnymi dla Couriera. couriermlm jest używany do konfigurowania,
zarządzania i prowadzenia pocztowej listy dyskusyjnej. Automatycznie
obsługuje żądania zapisywania i wypisywania oraz usuwa z listy
niedziałające adresy subskrybentów. Listy obsługiwane przez couriermlm
nie wymagają pracy administratora. couriermlm obsługuje digesty,
aliasy pocztowe tylko do wysyłania i listy moderowane.

%package maildrop
Summary:	Courier Integrated mail filter
Summary(pl.UTF-8):	Zintegrowany filtr poczty do Couriera
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description maildrop
This package installs Courier mail server's integrated mail filter.
You need to install this package if you want to be able to filter your
incoming mail.

%description maildrop -l pl.UTF-8
Ten pakiet zawiera zintegrowany filtr poczty dla Couriera. Jest
potrzebny do filtrowania przychodzącej poczty.

%package fax
Summary:	Courier fax support
Summary(pl.UTF-8):	Obsługa faksów dla Couriera
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	ghostscript
Requires:	groff
Requires:	netpbm-progs
#Requires:	/usr/bin/sendfax
# pdftops
Suggests:	poppler-progs

%description fax
This package adds support for faxing E-mail messages. It allows to
send fax messages simply by sending an E-mail to phonenumber@fax.

%description fax -l pl.UTF-8
Ten pakiet dodaje obsługę faksowania listów elektronicznych. Pozwala
wysyłać faksy wysyłając po prostu e-maila na numertelefonu@fax.

%prep
%setup -q
%{!?with_fam:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

cat >apache.conf <<EOF
Alias /webmail %{_imagedir}
<Directory %{_imagedir}>
	AllowOverride None
	Options None
	Allow from all
</Directory>
EOF

%build
%{__libtoolize}
# Change Makefile.am files and force recreate Makefile.in's.
OLDDIR=`pwd`
find -type f -a -name configure.ac | while read FILE; do
	cd "`dirname "$FILE"`"

	if [ -f Makefile.am ]; then
		sed -i -e '/_[L]DFLAGS=-static/d' Makefile.am
	fi

	%{__aclocal} -I m4
	%{__autoconf}
	if grep -q AC_CONFIG_HEADER configure.ac; then
		%{__autoheader}
	fi
	%{__automake}

	cd "$OLDDIR"
done

%configure \
	CERTTOOL=/usr/bin/certtool \
	GROPS=/usr/bin/grops \
	GS=/usr/bin/gs \
	PNMSCALE=/usr/bin/pnmscale \
	OPENSSL=/usr/bin/openssl \
	SENDFAX=/usr/bin/sendfax \
	--datadir=%{_datadir}/courier \
	--enable-imagedir=%{_imagedir} \
	--enable-imageurl=%{_imageurl} \
	--enable-mimetypes=/etc/mime.types \
	--with-certsdir=%{_certsdir} \
	--with-db=db \
	%{?with_gnutls:--with-gnutls} \
	--with-mailer=%{_sbindir}/sendmail \
	--with-mailgid=2 \
	--with-mailgroup=daemon \
	--with-mailuid=2 \
	--with-mailuser=daemon \
	--with-notice=unicode \
	%{!?with_socks:--without-socks}

%{__make} -j1
%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT
umask 022
install -d -p $RPM_BUILD_ROOT/etc/{cron.hourly,pam.d,rc.d/init.d} \
	$RPM_BUILD_ROOT{/usr/lib,%{_certsdir},%{_cgibindir},%{_webapps}/courier-webmail,%{_sysconfdir}/hosteddomains}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# fix pam problem
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/*.authpam
for X in imap esmtp pop3 webmail calendar
do
	cat > $RPM_BUILD_ROOT/etc/pam.d/$X <<'EOF'
#%PAM-1.0
auth	required	pam_unix.so shadow nullok
account	required	pam_unix.so
session	required	pam_unix.so
EOF
done

%{__make} install-perms

# Move webmail and webadmin to cgibindir
%{__mv} $RPM_BUILD_ROOT%{_libexecdir}/courier/webmail/webmail \
	$RPM_BUILD_ROOT%{_cgibindir}/webmail
%{__mv} $RPM_BUILD_ROOT%{_libexecdir}/courier/webmail/webadmin \
	$RPM_BUILD_ROOT%{_cgibindir}/webadmin

# install a cron job to clean out webmail's cache
install libs/sqwebmail/cron.cmd $RPM_BUILD_ROOT/etc/cron.hourly/courier-webmail-cleancache

# Move .html documentation to docdir; use common directory for all subpackages for references to work.
install -d $RPM_BUILD_ROOT%{_docdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/courier/htmldoc $RPM_BUILD_ROOT%{_docdir}/courier

# Manually set POP3DSTART and IMAPDSTART to yes, they'll go into a separate
# package, so after it's installed they should be runnable.

sed -i 's/^POP3DSTART.*/POP3DSTART=YES/' $RPM_BUILD_ROOT%{_sysconfdir}/pop3d.dist
sed -i 's/^POP3DSSLSTART.*/POP3DSSLSTART=YES/' $RPM_BUILD_ROOT%{_sysconfdir}/pop3d-ssl.dist
sed -i 's/^IMAPDSTART.*/IMAPDSTART=YES/' $RPM_BUILD_ROOT%{_sysconfdir}/imapd.dist
sed -i 's/^IMAPDSSLSTART.*/IMAPDSSLSTART=YES/' $RPM_BUILD_ROOT%{_sysconfdir}/imapd-ssl.dist

# Want to have esmtpd running by default
sed -i 's/^ESMTPDSTART.*/ESMTPDSTART=YES/' $RPM_BUILD_ROOT%{_sysconfdir}/esmtpd.dist

# run script from install-configure (make config files)
for confdist in `awk ' $5 == "config" && $1 ~ /\.dist$/ { print $1 }' <permissions.dat`
do %{__perl} ././sysconftool $RPM_BUILD_ROOT$confdist
done

# make locals, esmtpacceptmailfor.dir/default
touch $RPM_BUILD_ROOT%{_sysconfdir}/esmtpacceptmailfor.dir/default
touch $RPM_BUILD_ROOT%{_sysconfdir}/locals

# file with important options
cat > $RPM_BUILD_ROOT%{_sysconfdir}/bofh <<EOF
# enable this option if you want to pass bad converted mails
# opt BOFHBADMIME=accept
EOF

# Make password and unsecureok (files for webadmin)
touch $RPM_BUILD_ROOT%{_sysconfdir}/webadmin/password
touch $RPM_BUILD_ROOT%{_sysconfdir}/webadmin/unsecureok

# create file me to put localdomain
touch $RPM_BUILD_ROOT%{_sysconfdir}/me

# create calendarmode
touch $RPM_BUILD_ROOT%{_sysconfdir}/calendarmode

install courier.sysvinit $RPM_BUILD_ROOT/etc/rc.d/init.d/courier

# sendmail soft links
ln -sf %{_sbindir}/sendmail $RPM_BUILD_ROOT/usr/lib/sendmail

# fix rmail link (points to non-existing sendmail in %{_bindir}
ln -sf %{_sbindir}/sendmail $RPM_BUILD_ROOT%{_bindir}/rmail

# for apache
cp -p apache.conf $RPM_BUILD_ROOT%{_webapps}/courier-webmail/apache.conf
cp -p apache.conf $RPM_BUILD_ROOT%{_webapps}/courier-webmail/httpd.conf

# makedat is packaged in courier-authlib
%{__rm} $RPM_BUILD_ROOT%{_bindir}/makedat \
	$RPM_BUILD_ROOT%{_libexecdir}/courier/makedatprog \
	$RPM_BUILD_ROOT%{_datadir}/courier/makedat \
	$RPM_BUILD_ROOT%{_mandir}/man1/makedat.1
# remove unpackaged files
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/*.dist

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- courier < 0.45.5
echo
echo Directory with certificates has changed to %{_certsdir}
echo

%post
if [ "$1" = "1" ]; then
	[ -s %{_sysconfdir}/me ] || /bin/hostname -f > %{_sysconfdir}/me
	%banner -e %{name} <<'EOF'

Now courier will refuse to accept SMTP messages except to localhost
add hosts to %{_sysconfdir}/esmtpacceptmailfor.dir/default
run makeacceptmailfor

Add hosts to %{_sysconfdir}/locals you want to accept mail for
run makealiases

Enter user, who should receive mail for root, mailer-daemon and postmaster
into %{_sysconfdir}/aliases/system

Default maildir is in ~/Mail/Maildir

EOF
fi

/sbin/chkconfig --add courier
%service courier restart

%preun
if [ "$1" = "0" ]; then
	%service courier stop
	/sbin/chkconfig --del courier
fi

%post imapd
# TODO: use rc-scripts here
if [ -e %{_localstatedir}/tmp/imapd.pid ]; then
	%{_sbindir}/imapd stop
	%{_sbindir}/imapd start
else
	echo
	echo 'Type "%{_sbindir}/imapd start" to start imapd server'
	echo
fi
if [ -e %{_localstatedir}/tmp/imapd-ssl.pid ]; then
	%{_sbindir}/imapd-ssl stop
	%{_sbindir}/imapd-ssl start
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
else
	echo
	echo 'Type "%{_sbindir}/pop3d start" to start pop3d server'
	echo
fi
if [ -e %{_localstatedir}/tmp/pop3d-ssl.pid ]; then
	%{_sbindir}/pop3d-ssl stop
	%{_sbindir}/pop3d-ssl start
else
	echo
	echo 'Type "%{_sbindir}/pop3d-ssl start" to start pop3d-ssl server'
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
	echo 'Type "%{_sbindir}/webmaild start" to start webmail server'
	echo
fi

%preun webmail
if [ "$1" = "0" ]; then
	if [ -e %{_localstatedir}/tmp/sqwebmaild.pid ]; then
		%{_sbindir}/webmaild stop
	fi
fi

%triggerin webmail -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache courier-webmail

%triggerun webmail -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache courier-webmail

%triggerin webmail -- apache < 2.2.0, apache-base
%webapp_register httpd courier-webmail

%triggerun webmail -- apache < 2.2.0, apache-base
%webapp_unregister httpd courier-webmail

%triggerpostun webmail -- courier-webmail < 0.52.2-0.2
# migrate from apache-config macros
if [ -f /etc/courier/apache-courier.conf.rpmsave ]; then
	if [ -d /etc/apache/webapps.d ]; then
		cp -f %{_webapps}/courier-webmail/apache.conf{,.rpmnew}
		cp -f /etc/courier/apache-courier.conf.rpmsave %{_webapps}/courier-webmail/apache.conf
	fi

	if [ -d /etc/httpd/webapps.d ]; then
		cp -f %{_webapps}/courier-webmail/httpd.conf{,.rpmnew}
		cp -f /etc/courier/apache-courier.conf.rpmsave %{_webapps}/courier-webmail/httpd.conf
	fi
	rm -f /etc/courier/apache-courier.conf.rpmsave
fi

# migrating apache-config symlinks
if [ -L /etc/apache/conf.d/99_courier.conf ]; then
	rm -f /etc/apache/conf.d/99_courier.conf
	/usr/sbin/webapp register apache courier-webmail
	%service -q apache reload
fi
if [ -L /etc/httpd/httpd.conf/99_courier.conf ]; then
	rm -f /etc/httpd/httpd.conf/99_courier.conf
	/usr/sbin/webapp register httpd courier-webmail
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS BENCHMARKS COPYING ChangeLog INSTALL NEWS README TODO
# common:
# couriertcpd, couriertls are common TCP/TLS wrappers
# makemime used by sqwebmail, useful for maildrop
# reformime used by mlm, useful for maildrop
# deliverquota, sharedindex* are common for maildir
%attr(755,root,root) %{_bindir}/couriertls
%attr(755,root,root) %{_bindir}/deliverquota
%attr(755,root,root) %{_bindir}/makemime
%attr(755,root,root) %{_bindir}/mimegpg
%attr(755,root,root) %{_bindir}/reformime
%attr(755,root,root) %{_sbindir}/couriertcpd
%attr(755,root,root) %{_sbindir}/mkdhparams
%attr(755,root,root) %{_sbindir}/sharedindexinstall
%attr(755,root,root) %{_sbindir}/sharedindexsplit
%dir %{_libexecdir}/courier
%dir %{_datadir}/courier
%attr(755,root,root) %{_datadir}/courier/mkdhparams
%attr(755,daemon,daemon) %dir %{_sysconfdir}
%attr(750,daemon,daemon) %dir %{_certsdir}
%dir %{_docdir}/courier
%{_docdir}/courier/bg.png
%{_docdir}/courier/japanese_flag.png
%{_docdir}/courier/icon.gif
%{_docdir}/courier/manpage.css
%{_docdir}/courier/draft-varshavchik-*-smtpext.txt
%{_docdir}/courier/FAQ.html
%{_docdir}/courier/couriertcpd.html
%{_docdir}/courier/couriertls.html
%{_docdir}/courier/deliverquota.html
%{_docdir}/courier/documentation.html
%{_docdir}/courier/download.html
%{_docdir}/courier/index.html
%{_docdir}/courier/install.html
%{_docdir}/courier/layout.html
%{_docdir}/courier/links.html
%{_docdir}/courier/makedat.html
%{_docdir}/courier/makemime.html
%{_docdir}/courier/menu.html
%{_docdir}/courier/mimegpg.html
%{_docdir}/courier/mkdhparams.html
%{_docdir}/courier/modules.html
%{_docdir}/courier/reformime.html
%{_docdir}/courier/repo.html
%{_docdir}/courier/rpm.html
%{_docdir}/courier/socks.html
%{_docdir}/courier/status.html
%{_docdir}/courier/structures.html
%{_mandir}/man1/couriertcpd.1*
%{_mandir}/man1/couriertls.1*
%{_mandir}/man1/makemime.1*
%{_mandir}/man1/reformime.1*
%{_mandir}/man1/mimegpg.1*
%{_mandir}/man8/deliverquota.8*
%{_mandir}/man8/mkdhparams.8*

# MTA
%attr(6555,daemon,daemon) %{_bindir}/cancelmsg
%attr(755,root,root) %{_bindir}/courier-config
%attr(755,root,root) %{_bindir}/dotforward
%attr(2755,daemon,daemon) %{_bindir}/mailq
%attr(4755,root,root) %{_bindir}/rmail
%attr(755,root,root) %{_bindir}/testmxlookup
%attr(755,root,root) %{_sbindir}/aliaslookup
%attr(755,root,root) %{_sbindir}/courier
%attr(754,root,daemon) %{_sbindir}/makealiases
%attr(755,root,root) %{_sbindir}/makehosteddomains
%attr(755,root,root) %{_sbindir}/showconfig
%attr(754,root,daemon) %{_sbindir}/showmodules
%attr(4755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) /usr/lib/sendmail
%attr(754,daemon,daemon) %{_libexecdir}/courier/aliascombine
%attr(754,daemon,daemon) %{_libexecdir}/courier/aliascreate
%attr(754,daemon,daemon) %{_libexecdir}/courier/aliasexp
%attr(754,daemon,daemon) %{_libexecdir}/courier/courierd
%attr(754,daemon,daemon) %{_libexecdir}/courier/submit
%attr(4554,daemon,daemon) %{_libexecdir}/courier/submitmkdir
%attr(755,root,root) %{_datadir}/courier/courierctl.start
%attr(754,root,daemon) %{_datadir}/courier/makealiases
%attr(755,root,root) %{_datadir}/courier/makehosteddomains
%attr(755,daemon,daemon) %dir %{_sysconfdir}/shared
%attr(755,daemon,daemon) %dir %{_sysconfdir}/shared.tmp
%attr(754,root,root) /etc/rc.d/init.d/courier
%attr(755,bin,bin) %dir %{_localstatedir}
%attr(755,daemon,daemon) %dir %{_localstatedir}/track
%{_docdir}/courier/aliases.html
%{_docdir}/courier/aliaslookup.html
%{_docdir}/courier/cancelmsg.html
%{_docdir}/courier/courier.html
%{_docdir}/courier/courierd.html
%{_docdir}/courier/dot-courier.html
%{_docdir}/courier/dot-forward.html
%{_docdir}/courier/mailq.html
%{_docdir}/courier/makealiases.html
%{_docdir}/courier/makehosteddomains.html
%{_docdir}/courier/queue.html
%{_docdir}/courier/sendmail.html
%{_docdir}/courier/submit.html
%{_docdir}/courier/testmxlookup.html
%{_mandir}/man1/cancelmsg.1*
%{_mandir}/man1/dot-forward.1*
%{_mandir}/man1/dotforward.1*
%{_mandir}/man1/mailq.1*
%{_mandir}/man1/rmail.1*
%{_mandir}/man1/sendmail.1*
%{_mandir}/man1/testmxlookup.1*
%{_mandir}/man5/dot-courier.5*
%{_mandir}/man7/localmailfilter.7*
%{_mandir}/man8/aliaslookup.8*
%{_mandir}/man8/courier.8*
%{_mandir}/man8/makealiases.8*
%{_mandir}/man8/makehosteddomains.8*
%{_mandir}/man8/submit.8*
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bofh
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/courierd
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enablefiltering
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/locals
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/me
%attr(755,daemon,daemon) %dir %{_sysconfdir}/aliasdir
%attr(750,daemon,daemon) %dir %{_sysconfdir}/aliases
%attr(640,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/aliases/system
%attr(755,daemon,daemon) %dir %{_sysconfdir}/hosteddomains
%attr(755,daemon,daemon) %dir %{_sysconfdir}/smtpaccess
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/smtpaccess/default
%{_sysconfdir}/quotawarnmsg.example
%dir %{_datadir}/courier/courierwebadmin
%{_datadir}/courier/courierwebadmin/admin-15*

# LDAP configuration
%attr(744,daemon,daemon) %{_sbindir}/courierldapaliasd
%attr(640,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ldapaliasrc
%{_docdir}/courier/courierldapaliasd.html
%{_mandir}/man8/courierldapaliasd.8*

# filters
%attr(755,root,root) %{_bindir}/verifysmtp
%attr(754,root,daemon) %{_sbindir}/courierfilter
%attr(754,root,daemon) %{_sbindir}/filterctl
%attr(755,root,root) %{_libexecdir}/courier/courierfilter
%dir %{_libexecdir}/courier/filters
%attr(755,root,root) %{_libexecdir}/courier/filters/dupfilter
%attr(755,root,root) %{_libexecdir}/courier/filters/perlfilter
%attr(755,root,root) %{_libexecdir}/courier/filters/ratefilter
%attr(755,root,root) %{_libexecdir}/courier/filters/verifyfilter
%attr(754,root,daemon) %{_datadir}/courier/filterctl
%attr(755,root,root) %{_datadir}/courier/perlfilter-*.pl
%attr(755,root,root) %{_datadir}/courier/verifysender
%attr(755,root,root) %{_datadir}/courier/verifysenderfull
%attr(750,daemon,daemon) %dir %{_sysconfdir}/filters
%attr(750,daemon,daemon) %dir %{_sysconfdir}/filters/active
%attr(750,daemon,daemon) %dir %{_localstatedir}/allfilters
%attr(750,daemon,daemon) %dir %{_localstatedir}/filters
%attr(770,daemon,daemon) %dir %{_localstatedir}/tmp
%attr(750,daemon,daemon) %dir %{_localstatedir}/msgs
%attr(750,daemon,daemon) %dir %{_localstatedir}/msgq
%{_docdir}/courier/courierfilter.html
%{_docdir}/courier/courierperlfilter.html
%{_docdir}/courier/dupfilter.html
%{_docdir}/courier/ratefilter.html
%{_docdir}/courier/verifyfilter.html
%{_mandir}/man8/courierfilter.8*
%{_mandir}/man8/courierperlfilter.8*
%{_mandir}/man8/dupfilter.8*
%{_mandir}/man8/filterctl.8*
%{_mandir}/man8/ratefilter.8*
%{_mandir}/man8/verifyfilter.8*
%{_mandir}/man8/verifysmtp.8*

# module.dsn
%dir %{_libexecdir}/courier/modules/dsn
%attr(755,root,root) %{_libexecdir}/courier/modules/dsn/courierdsn
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/module.dsn
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsndelayed.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsndelivered.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsnfailed.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsnrelayed.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsnfooter.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsnsubjectnotice.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsnsubjectwarn.txt
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dsnheader.txt
%{_docdir}/courier/courierdsn.html

# module.esmtp
%attr(755,root,root) %{_bindir}/addcr
%attr(755,root,root) %{_sbindir}/courieresmtpd
%attr(755,root,root) %{_sbindir}/esmtpd
%attr(755,root,root) %{_sbindir}/esmtpd-msa
%attr(755,root,root) %{_sbindir}/esmtpd-ssl
%attr(755,root,root) %{_sbindir}/makeacceptmailfor
%attr(755,root,root) %{_sbindir}/makepercentrelay
%attr(755,root,root) %{_sbindir}/makesmtpaccess
%attr(755,root,root) %{_sbindir}/makesmtpaccess-msa
%attr(755,root,root) %{_sbindir}/mkesmtpdcert
%dir %{_libexecdir}/courier/modules/esmtp
%attr(754,root,daemon) %{_libexecdir}/courier/modules/esmtp/courieresmtp
%attr(754,root,daemon) %{_libexecdir}/courier/modules/esmtp/courieresmtpd
%attr(755,root,root) %{_libexecdir}/courier/modules/esmtp/addcr
%attr(755,root,root) %{_datadir}/courier/esmtpd
%attr(755,root,root) %{_datadir}/courier/esmtpd-ssl
%attr(755,root,root) %{_datadir}/courier/makeacceptmailfor
%attr(755,root,root) %{_datadir}/courier/makepercentrelay
%attr(755,root,root) %{_datadir}/courier/makesmtpaccess
%attr(755,root,root) %{_datadir}/courier/mkesmtpdcert
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/esmtp
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/module.esmtp
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esmtpd
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esmtpd-msa
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esmtpd-ssl
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esmtpd.cnf
%attr(600,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esmtpauthclient
%attr(755,daemon,daemon) %dir %{_sysconfdir}/esmtpacceptmailfor.dir
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/esmtpacceptmailfor.dir/default
%attr(755,daemon,daemon) %dir %{_sysconfdir}/esmtppercentrelay.dir
%{_docdir}/courier/esmtp.html
%{_docdir}/courier/esmtpd.html
%{_docdir}/courier/makeacceptmailfor.html
%{_docdir}/courier/makepercentrelay.html
%{_docdir}/courier/makesmtpaccess.html
%{_docdir}/courier/mkesmtpdcert.html
%{_mandir}/man8/esmtpd.8*
%{_mandir}/man8/esmtpd-msa.8*
%{_mandir}/man8/makeacceptmailfor.8*
%{_mandir}/man8/makepercentrelay.8*
%{_mandir}/man8/makesmtpaccess.8*
%{_mandir}/man8/makesmtpaccess-msa.8*
%{_mandir}/man8/mkesmtpdcert.8*

# module.local
%attr(755,root,root) %{_bindir}/preline
%dir %{_libexecdir}/courier/modules/local
%attr(755,root,root) %{_libexecdir}/courier/modules/local/courierdeliver
%attr(755,root,root) %{_libexecdir}/courier/modules/local/courierlocal
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/module.local
%{_docdir}/courier/local.html
%{_docdir}/courier/localmailfilter.html
%{_docdir}/courier/preline.html
%{_mandir}/man1/preline.1*

# module.uucp
%attr(755,root,root) %{_sbindir}/makeuucpneighbors
%dir %{_libexecdir}/courier/modules
%dir %{_libexecdir}/courier/modules/uucp
%attr(755,root,root) %{_libexecdir}/courier/modules/uucp/courieruucp
%attr(755,root,root) %{_datadir}/courier/makeuucpneighbors
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/module.uucp
%{_docdir}/courier/courieruucp.html
%{_mandir}/man8/courieruucp.8*
%{_mandir}/man8/makeuucpneighbors.8*

%files pop3d
%defattr(644,root,root,755)
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pop3d
%attr(600,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pop3d.cnf
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pop3d-ssl
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/pop3
%attr(755,root,root) %{_sbindir}/mkpop3dcert
%attr(755,root,root) %{_sbindir}/pop3d
%attr(755,root,root) %{_sbindir}/pop3d-ssl
%attr(755,root,root) %{_libexecdir}/courier/courierpop3d
%attr(755,root,root) %{_libexecdir}/courier/courierpop3login
%attr(755,root,root) %{_datadir}/courier/mkpop3dcert
%attr(755,root,root) %{_datadir}/courier/pop3d
%attr(755,root,root) %{_datadir}/courier/pop3d-ssl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-45pop3.pl
%{_datadir}/courier/courierwebadmin/admin-45pop3.html
%{_docdir}/courier/courierpop3d.html
%{_docdir}/courier/mkpop3dcert.html
%{_docdir}/courier/pop3d.html
%{_mandir}/man8/courierpop3d.8*
%{_mandir}/man8/courierpop3login.8*
%{_mandir}/man8/mkpop3dcert.8*
%{_mandir}/man8/pop3d.8*
%{_mandir}/man8/pop3d-ssl.8*

%files imapd
%defattr(644,root,root,755)
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imapd
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imapd-ssl
%attr(600,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imapd.cnf
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/imap
%attr(755,root,root) %{_bindir}/imapd
%attr(755,root,root) %{_sbindir}/imapd
%attr(755,root,root) %{_sbindir}/imapd-ssl
%attr(755,root,root) %{_sbindir}/makeimapaccess
%attr(755,root,root) %{_sbindir}/mkimapdcert
%attr(755,root,root) %{_libexecdir}/courier/imaplogin
%attr(755,root,root) %{_datadir}/courier/imapd
%attr(755,root,root) %{_datadir}/courier/imapd-ssl
%attr(755,root,root) %{_datadir}/courier/makeimapaccess
%attr(755,root,root) %{_datadir}/courier/mkimapdcert
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-40imap.pl
%{_datadir}/courier/courierwebadmin/admin-40imap.html
%{_docdir}/courier/imapd.html
%{_docdir}/courier/makeimapaccess.html
%{_docdir}/courier/mkimapdcert.html
%{_mandir}/man8/imapd.8*
%{_mandir}/man8/makeimapaccess.8*
%{_mandir}/man8/mkimapdcert.8*

%files webadmin
%defattr(644,root,root,755)
# suid root to cgi-bin??? and it's not secured by apache config!
%attr(4755,root,root) %{_cgibindir}/webadmin
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin/added
%attr(700,daemon,daemon) %dir %{_sysconfdir}/webadmin/removed
%attr(400,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/webadmin/password
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/webadmin/unsecureok
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-main.pl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-save.pl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-cancel.pl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-[0235]*.pl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-10password.pl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/dumpenv.pl
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/webadmin.pl
%{_datadir}/courier/courierwebadmin/admin-[0235]*.html
%{_datadir}/courier/courierwebadmin/admin-10password.html
%{_datadir}/courier/courierwebadmin/admin-main.html
%{_datadir}/courier/courierwebadmin/admin-save.html
%{_datadir}/courier/courierwebadmin/login.html
%{_datadir}/courier/courierwebadmin/notsupp.html
%{_datadir}/courier/courierwebadmin/unsecure.html
%{_datadir}/courier/courierwebadmin/webadmin.pm

%files webmail
%defattr(644,root,root,755)
%doc libs/gpglib/README.html
%attr(755,root,root) %{_cgibindir}/webmail
%attr(755,root,root) /etc/cron.hourly/courier-webmail-cleancache
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/webmail
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/calendar
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/calendarmode
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ldapaddressbook
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sqwebmaild
%attr(755,root,root) %{_sbindir}/webgpg
%attr(755,root,root) %{_sbindir}/webmaild
%attr(755,root,root) %{_libexecdir}/courier/pcpd
%attr(755,root,root) %{_libexecdir}/courier/sqwebmaild
%attr(755,root,root) %{_libexecdir}/courier/sqwebpasswd
%dir %{_datadir}/courier/sqwebmail
%dir %{_datadir}/courier/sqwebmail/html
%dir %{_datadir}/courier/sqwebmail/html/en-us
%{_datadir}/courier/sqwebmail/html/en
%{_datadir}/courier/sqwebmail/images
%config %{_datadir}/courier/sqwebmail/html/en-us/[CILT]*
%{_datadir}/courier/sqwebmail/html/en-us/*.html
%{_datadir}/courier/sqwebmail/html/en-us/*.txt
%attr(755,root,root) %{_datadir}/courier/sqwebmail/cleancache.pl
%attr(755,root,root) %{_datadir}/courier/sqwebmail/ldapsearch
%attr(755,root,root) %{_datadir}/courier/sqwebmail/sendit.sh
%attr(755,root,root) %{_datadir}/courier/sqwebmail/webgpg
%attr(755,root,root) %{_datadir}/courier/courierwebadmin/admin-47webmail.pl
%{_datadir}/courier/courierwebadmin/admin-47webmail.html
%attr(755,bin,daemon) %dir %{_localstatedir}/calendar
%attr(700,bin,daemon) %dir %{_localstatedir}/calendar/localcache
%attr(750,bin,daemon) %dir %{_localstatedir}/calendar/private
%attr(755,bin,daemon) %dir %{_localstatedir}/calendar/public
%attr(700,bin,bin) %dir %{_localstatedir}/webmail-logincache
%dir %attr(750,root,http) %{_webapps}/courier-webmail
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/courier-webmail/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/courier-webmail/httpd.conf
%{_docdir}/courier/pcp_README.html

%files webmlm
%defattr(644,root,root,755)
%attr(700,daemon,daemon) %{_sysconfdir}/webmlmrc
%attr(755,root,root) %{_bindir}/webmlmd
%attr(755,root,root) %{_bindir}/webmlmd.rc
%dir %{_libexecdir}/courier/webmail
%attr(755,root,root) %{_libexecdir}/courier/webmail/webmlm
%{_docdir}/courier/webmlmd.html
%{_mandir}/man1/webmlmd.1*

%files maildrop
%defattr(644,root,root,755)
%attr(644,daemon,daemon) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/maildrop
%attr(755,root,root) %{_bindir}/lockmail
%attr(755,root,root) %{_bindir}/mailbot
%attr(4755,root,root) %{_bindir}/maildrop
%attr(755,root,root) %{_bindir}/reformail
%{_docdir}/courier/lockmail.html
%{_docdir}/courier/mailbot.html
%{_docdir}/courier/maildrop*.html
%{_docdir}/courier/reformail.html
%{_mandir}/man1/lockmail.1*
%{_mandir}/man1/mailbot.1*
%{_mandir}/man1/maildrop.1*
%{_mandir}/man1/reformail.1*
%{_mandir}/man7/maildropex.7*
%{_mandir}/man7/maildropfilter.7*
%{_mandir}/man7/maildropgdbm.7*

%files maildir-tools
%defattr(644,root,root,755)
%doc libs/maildir/README.*.html
%attr(755,root,root) %{_bindir}/maildirmake
%attr(755,root,root) %{_bindir}/maildirkw
%attr(755,root,root) %{_bindir}/maildiracl
%{_docdir}/courier/maildir*.html
%{_mandir}/man1/maildirmake.1*
%{_mandir}/man1/maildirkw.1*
%{_mandir}/man1/maildiracl.1*
%{_mandir}/man5/maildir.5*
%{_mandir}/man7/maildirquota.7*

%files mlm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/couriermlm
%{_datadir}/courier/couriermlm
%{_docdir}/courier/couriermlm.html
%{_mandir}/man1/couriermlm.1*

%files fax
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faxcoverpage.tr
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faxnotifyrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faxrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/module.fax
%dir %{_libexecdir}/courier/modules/fax
%attr(755,root,root) %{_libexecdir}/courier/modules/fax/courierfax
%dir %{_datadir}/courier/faxmail
%{_datadir}/courier/faxmail/*.filter
%{_datadir}/courier/faxmail/coverpage
%{_datadir}/courier/faxmail/init
%{_datadir}/courier/faxmail/new_fax
%{_docdir}/courier/courierfax.html
%{_mandir}/man8/courierfax.8*
