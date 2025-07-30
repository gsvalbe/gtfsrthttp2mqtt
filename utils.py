def parse_short_name(feed, trip_id, route_id, otp_data):
    if otp_data == None:
        return ""

    feed_scoped_id = feed + ":" + route_id
    if feed_scoped_id not in otp_data:
        return ""
    return otp_data[feed_scoped_id]["shortName"] or ""

def parse_color(feed, trip_id, route_id, otp_data):
    if otp_data == None:
        return ""

    feed_scoped_id = feed + ":" + route_id
    if feed_scoped_id not in otp_data:
        return ""
    return otp_data[feed + ":" + route_id]["color"] or ""

def parse_mode(feed, trip_id, route_id, otp_data):
    if otp_data == None:
        return ""

    feed_scoped_id = feed + ":" + route_id
    if feed_scoped_id not in otp_data:
        return ""
    return otp_data[feed + ":" + route_id]["mode"] or ""

def get_OTP_query(feed):
    return """
        {
            routes(feeds: [\"%s\"]) {
                gtfsId
                shortName
                color
                textColor
                mode
            }
        }
        """ % feed
