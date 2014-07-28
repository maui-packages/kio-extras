# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       kde5-kio-extras
Summary:    Additional components to increase the functionality of KIO Framework
Version:    5.0.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source1:    kde.pam
Source100:  kde5-kio-extras.yaml
Source101:  kde5-kio-extras-rpmlintrc
Requires:   kde5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-umbrella
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kdnssd-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  phonon-qt5-devel
BuildRequires:  bzip2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  lzma-devel


%description
Additional components to increase the functionality of KIO Framework.




%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
# Remove libmolletnetwork.so - we don't have headers for it anyway and having
# a -devel package just because of this does not make sense
rm %{buildroot}/%{_kde5_libdir}/libmolletnetwork.so
# << install post






%files
%defattr(-,root,root,-)
%{_kde5_bindir}/ktrash5
%{_kde5_libdir}/libmolletnetwork.so.*
%{_kde5_plugindir}/*.so
%{_kde5_datadir}/*
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservicetypes5/thumbcreator.desktop
%{_datadir}/dbus-1/interfaces/kf5_org.kde.network.kioslavenotifier.xml
%{_datadir}/mime/packages/kf5_network.xml
%{_datadir}/doc/HTML/en/kioslave5
%{_datadir}/doc/HTML/en/kcontrol
%{_datadir}/config.kcfg/jpegcreatorsettings.kcfg
# >> files
# << files


