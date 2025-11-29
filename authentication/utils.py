def mask_email(email: str) -> str:
    """Returns a string with a partially censored local part of given email address."""
    local_part, domain = email.split("@")
    masked_local = (
        f"{local_part[0]}{'*' * (len(local_part) - 2)}{local_part[-1]}"
        if len(local_part) > 2
        else "*" * len(local_part)
    )
    return "%s@%s" % (masked_local, domain)
