import ldap

def authanticate(username, password):
    conn = ldap.initialize('ldap://kiyiemniyeti.local')
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    try:
        result = conn.simple_bind_s(username + '@kiyiemniyeti.local', password)

    except ldap.INVALID_CREDENTIALS:
        return False
    except ldap.SERVER_DOWN:
        return False
    finally:
        conn.unbind_s()
    
    return True


