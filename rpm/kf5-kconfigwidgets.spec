%global kf5_version 5.116.0

Name:    opt-kf5-kconfigwidgets
Version: 5.116.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon for creating configuration dialogs

License: GPLv2+ and LGPLv2+ and MIT
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  opt-kf5-kcodecs-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kguiaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros

# KColorScheme requires color schemes to be installed
# https://pagure.io/fedora-workstation/issue/314
#Requires:       plasma-breeze-common

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-kf5-kcodecs-devel >= %{kf5_version}
Requires:       opt-kf5-kconfig-devel >= %{kf5_version}
Requires:       opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5 -DWITH_KAUTH=OFF
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-man --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kconfigwidgets*
%{_opt_kf5_libdir}/libKF5ConfigWidgets.so.*
## fixme: %%lang'ify these -- rex
%{_opt_kf5_datadir}/locale/*/kf5_entry.desktop
%{_opt_kf5_qtplugindir}/designer/*5widgets.so

%files devel
%{_opt_kf5_bindir}/preparetips5

%{_opt_kf5_includedir}/KF5/KConfigWidgets/
%{_opt_kf5_libdir}/libKF5ConfigWidgets.so
%{_opt_kf5_libdir}/cmake/KF5ConfigWidgets/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KConfigWidgets.pri
