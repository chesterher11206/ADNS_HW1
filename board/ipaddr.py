import geoip2.database


def ip2addr(ip):
    reader = geoip2.database.Reader('blog/GeoLite2-City.mmdb')
    response = reader.city(ip)

    province = ''
    city = ''
    try:
        country = response.country.names["zh-CN"]
        province = response.subdivisions.most_specific.names["zh-CN"]
        city = response.city.names["zh-CN"]
    except:
        pass
    if country != '中國':
        return country
    if province and city:
        if province == city or city in province:
            return province
        return '%s%s' %(province, city)
    elif province and not city:
        return province
    else:
        return country