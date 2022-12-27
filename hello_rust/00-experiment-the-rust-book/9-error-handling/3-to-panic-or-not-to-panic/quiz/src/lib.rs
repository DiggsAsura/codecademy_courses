fn parse_flag_v1(flag: &str) -> Result<String, String> {
    match flag.strip_prefix("--") {
        Some(no_dash)   => Ok(no_dash.to_string()),
        None            => Err(format!("Invalid flag {flag}"))
    }
}
