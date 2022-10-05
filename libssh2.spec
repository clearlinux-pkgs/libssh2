#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5CC908FDB71E12C2 (daniel@haxx.se)
#
Name     : libssh2
Version  : 1.10.0
Release  : 19
URL      : https://www.libssh2.org/download/libssh2-1.10.0.tar.gz
Source0  : https://www.libssh2.org/download/libssh2-1.10.0.tar.gz
Source1  : https://www.libssh2.org/download/libssh2-1.10.0.tar.gz.asc
Summary  : Library for SSH-based communication
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libssh2-lib = %{version}-%{release}
Requires: libssh2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(openssl)
BuildRequires : zlib-dev

%description
libssh2 - SSH2 library
======================
libssh2 is a library implementing the SSH2 protocol, available under
the revised BSD license.

%package dev
Summary: dev components for the libssh2 package.
Group: Development
Requires: libssh2-lib = %{version}-%{release}
Provides: libssh2-devel = %{version}-%{release}
Requires: libssh2 = %{version}-%{release}

%description dev
dev components for the libssh2 package.


%package lib
Summary: lib components for the libssh2 package.
Group: Libraries
Requires: libssh2-license = %{version}-%{release}

%description lib
lib components for the libssh2 package.


%package license
Summary: license components for the libssh2 package.
Group: Default

%description license
license components for the libssh2 package.


%prep
%setup -q -n libssh2-1.10.0
cd %{_builddir}/libssh2-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664932154
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664932154
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libssh2
cp %{_builddir}/libssh2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libssh2/19b306b372fdae0f6390c0d4192c2a8f7973dac7 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libssh2.h
/usr/include/libssh2_publickey.h
/usr/include/libssh2_sftp.h
/usr/lib64/libssh2.so
/usr/lib64/pkgconfig/libssh2.pc
/usr/share/man/man3/libssh2_agent_connect.3
/usr/share/man/man3/libssh2_agent_disconnect.3
/usr/share/man/man3/libssh2_agent_free.3
/usr/share/man/man3/libssh2_agent_get_identity.3
/usr/share/man/man3/libssh2_agent_get_identity_path.3
/usr/share/man/man3/libssh2_agent_init.3
/usr/share/man/man3/libssh2_agent_list_identities.3
/usr/share/man/man3/libssh2_agent_set_identity_path.3
/usr/share/man/man3/libssh2_agent_userauth.3
/usr/share/man/man3/libssh2_banner_set.3
/usr/share/man/man3/libssh2_base64_decode.3
/usr/share/man/man3/libssh2_channel_close.3
/usr/share/man/man3/libssh2_channel_direct_tcpip.3
/usr/share/man/man3/libssh2_channel_direct_tcpip_ex.3
/usr/share/man/man3/libssh2_channel_eof.3
/usr/share/man/man3/libssh2_channel_exec.3
/usr/share/man/man3/libssh2_channel_flush.3
/usr/share/man/man3/libssh2_channel_flush_ex.3
/usr/share/man/man3/libssh2_channel_flush_stderr.3
/usr/share/man/man3/libssh2_channel_forward_accept.3
/usr/share/man/man3/libssh2_channel_forward_cancel.3
/usr/share/man/man3/libssh2_channel_forward_listen.3
/usr/share/man/man3/libssh2_channel_forward_listen_ex.3
/usr/share/man/man3/libssh2_channel_free.3
/usr/share/man/man3/libssh2_channel_get_exit_signal.3
/usr/share/man/man3/libssh2_channel_get_exit_status.3
/usr/share/man/man3/libssh2_channel_handle_extended_data.3
/usr/share/man/man3/libssh2_channel_handle_extended_data2.3
/usr/share/man/man3/libssh2_channel_ignore_extended_data.3
/usr/share/man/man3/libssh2_channel_open_ex.3
/usr/share/man/man3/libssh2_channel_open_session.3
/usr/share/man/man3/libssh2_channel_process_startup.3
/usr/share/man/man3/libssh2_channel_read.3
/usr/share/man/man3/libssh2_channel_read_ex.3
/usr/share/man/man3/libssh2_channel_read_stderr.3
/usr/share/man/man3/libssh2_channel_receive_window_adjust.3
/usr/share/man/man3/libssh2_channel_receive_window_adjust2.3
/usr/share/man/man3/libssh2_channel_request_pty.3
/usr/share/man/man3/libssh2_channel_request_pty_ex.3
/usr/share/man/man3/libssh2_channel_request_pty_size.3
/usr/share/man/man3/libssh2_channel_request_pty_size_ex.3
/usr/share/man/man3/libssh2_channel_send_eof.3
/usr/share/man/man3/libssh2_channel_set_blocking.3
/usr/share/man/man3/libssh2_channel_setenv.3
/usr/share/man/man3/libssh2_channel_setenv_ex.3
/usr/share/man/man3/libssh2_channel_shell.3
/usr/share/man/man3/libssh2_channel_subsystem.3
/usr/share/man/man3/libssh2_channel_wait_closed.3
/usr/share/man/man3/libssh2_channel_wait_eof.3
/usr/share/man/man3/libssh2_channel_window_read.3
/usr/share/man/man3/libssh2_channel_window_read_ex.3
/usr/share/man/man3/libssh2_channel_window_write.3
/usr/share/man/man3/libssh2_channel_window_write_ex.3
/usr/share/man/man3/libssh2_channel_write.3
/usr/share/man/man3/libssh2_channel_write_ex.3
/usr/share/man/man3/libssh2_channel_write_stderr.3
/usr/share/man/man3/libssh2_channel_x11_req.3
/usr/share/man/man3/libssh2_channel_x11_req_ex.3
/usr/share/man/man3/libssh2_exit.3
/usr/share/man/man3/libssh2_free.3
/usr/share/man/man3/libssh2_hostkey_hash.3
/usr/share/man/man3/libssh2_init.3
/usr/share/man/man3/libssh2_keepalive_config.3
/usr/share/man/man3/libssh2_keepalive_send.3
/usr/share/man/man3/libssh2_knownhost_add.3
/usr/share/man/man3/libssh2_knownhost_addc.3
/usr/share/man/man3/libssh2_knownhost_check.3
/usr/share/man/man3/libssh2_knownhost_checkp.3
/usr/share/man/man3/libssh2_knownhost_del.3
/usr/share/man/man3/libssh2_knownhost_free.3
/usr/share/man/man3/libssh2_knownhost_get.3
/usr/share/man/man3/libssh2_knownhost_init.3
/usr/share/man/man3/libssh2_knownhost_readfile.3
/usr/share/man/man3/libssh2_knownhost_readline.3
/usr/share/man/man3/libssh2_knownhost_writefile.3
/usr/share/man/man3/libssh2_knownhost_writeline.3
/usr/share/man/man3/libssh2_poll.3
/usr/share/man/man3/libssh2_poll_channel_read.3
/usr/share/man/man3/libssh2_publickey_add.3
/usr/share/man/man3/libssh2_publickey_add_ex.3
/usr/share/man/man3/libssh2_publickey_init.3
/usr/share/man/man3/libssh2_publickey_list_fetch.3
/usr/share/man/man3/libssh2_publickey_list_free.3
/usr/share/man/man3/libssh2_publickey_remove.3
/usr/share/man/man3/libssh2_publickey_remove_ex.3
/usr/share/man/man3/libssh2_publickey_shutdown.3
/usr/share/man/man3/libssh2_scp_recv.3
/usr/share/man/man3/libssh2_scp_recv2.3
/usr/share/man/man3/libssh2_scp_send.3
/usr/share/man/man3/libssh2_scp_send64.3
/usr/share/man/man3/libssh2_scp_send_ex.3
/usr/share/man/man3/libssh2_session_abstract.3
/usr/share/man/man3/libssh2_session_banner_get.3
/usr/share/man/man3/libssh2_session_banner_set.3
/usr/share/man/man3/libssh2_session_block_directions.3
/usr/share/man/man3/libssh2_session_callback_set.3
/usr/share/man/man3/libssh2_session_disconnect.3
/usr/share/man/man3/libssh2_session_disconnect_ex.3
/usr/share/man/man3/libssh2_session_flag.3
/usr/share/man/man3/libssh2_session_free.3
/usr/share/man/man3/libssh2_session_get_blocking.3
/usr/share/man/man3/libssh2_session_get_timeout.3
/usr/share/man/man3/libssh2_session_handshake.3
/usr/share/man/man3/libssh2_session_hostkey.3
/usr/share/man/man3/libssh2_session_init.3
/usr/share/man/man3/libssh2_session_init_ex.3
/usr/share/man/man3/libssh2_session_last_errno.3
/usr/share/man/man3/libssh2_session_last_error.3
/usr/share/man/man3/libssh2_session_method_pref.3
/usr/share/man/man3/libssh2_session_methods.3
/usr/share/man/man3/libssh2_session_set_blocking.3
/usr/share/man/man3/libssh2_session_set_last_error.3
/usr/share/man/man3/libssh2_session_set_timeout.3
/usr/share/man/man3/libssh2_session_startup.3
/usr/share/man/man3/libssh2_session_supported_algs.3
/usr/share/man/man3/libssh2_sftp_close.3
/usr/share/man/man3/libssh2_sftp_close_handle.3
/usr/share/man/man3/libssh2_sftp_closedir.3
/usr/share/man/man3/libssh2_sftp_fsetstat.3
/usr/share/man/man3/libssh2_sftp_fstat.3
/usr/share/man/man3/libssh2_sftp_fstat_ex.3
/usr/share/man/man3/libssh2_sftp_fstatvfs.3
/usr/share/man/man3/libssh2_sftp_fsync.3
/usr/share/man/man3/libssh2_sftp_get_channel.3
/usr/share/man/man3/libssh2_sftp_init.3
/usr/share/man/man3/libssh2_sftp_last_error.3
/usr/share/man/man3/libssh2_sftp_lstat.3
/usr/share/man/man3/libssh2_sftp_mkdir.3
/usr/share/man/man3/libssh2_sftp_mkdir_ex.3
/usr/share/man/man3/libssh2_sftp_open.3
/usr/share/man/man3/libssh2_sftp_open_ex.3
/usr/share/man/man3/libssh2_sftp_opendir.3
/usr/share/man/man3/libssh2_sftp_read.3
/usr/share/man/man3/libssh2_sftp_readdir.3
/usr/share/man/man3/libssh2_sftp_readdir_ex.3
/usr/share/man/man3/libssh2_sftp_readlink.3
/usr/share/man/man3/libssh2_sftp_realpath.3
/usr/share/man/man3/libssh2_sftp_rename.3
/usr/share/man/man3/libssh2_sftp_rename_ex.3
/usr/share/man/man3/libssh2_sftp_rewind.3
/usr/share/man/man3/libssh2_sftp_rmdir.3
/usr/share/man/man3/libssh2_sftp_rmdir_ex.3
/usr/share/man/man3/libssh2_sftp_seek.3
/usr/share/man/man3/libssh2_sftp_seek64.3
/usr/share/man/man3/libssh2_sftp_setstat.3
/usr/share/man/man3/libssh2_sftp_shutdown.3
/usr/share/man/man3/libssh2_sftp_stat.3
/usr/share/man/man3/libssh2_sftp_stat_ex.3
/usr/share/man/man3/libssh2_sftp_statvfs.3
/usr/share/man/man3/libssh2_sftp_symlink.3
/usr/share/man/man3/libssh2_sftp_symlink_ex.3
/usr/share/man/man3/libssh2_sftp_tell.3
/usr/share/man/man3/libssh2_sftp_tell64.3
/usr/share/man/man3/libssh2_sftp_unlink.3
/usr/share/man/man3/libssh2_sftp_unlink_ex.3
/usr/share/man/man3/libssh2_sftp_write.3
/usr/share/man/man3/libssh2_trace.3
/usr/share/man/man3/libssh2_trace_sethandler.3
/usr/share/man/man3/libssh2_userauth_authenticated.3
/usr/share/man/man3/libssh2_userauth_hostbased_fromfile.3
/usr/share/man/man3/libssh2_userauth_hostbased_fromfile_ex.3
/usr/share/man/man3/libssh2_userauth_keyboard_interactive.3
/usr/share/man/man3/libssh2_userauth_keyboard_interactive_ex.3
/usr/share/man/man3/libssh2_userauth_list.3
/usr/share/man/man3/libssh2_userauth_password.3
/usr/share/man/man3/libssh2_userauth_password_ex.3
/usr/share/man/man3/libssh2_userauth_publickey.3
/usr/share/man/man3/libssh2_userauth_publickey_fromfile.3
/usr/share/man/man3/libssh2_userauth_publickey_fromfile_ex.3
/usr/share/man/man3/libssh2_userauth_publickey_frommemory.3
/usr/share/man/man3/libssh2_version.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libssh2.so.1
/usr/lib64/libssh2.so.1.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libssh2/19b306b372fdae0f6390c0d4192c2a8f7973dac7
