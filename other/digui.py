data = {
    "tracking_info": [
        "test05: content_content",
        "test01_begin",
        "   test01_content_content",
        "test01_end",
        "test02_begin",
        "   test03_begin",
        "       test03_content_content",
        "       test06: content_content",
        "   test03_end",
        "   test02_content_content",
        "test02_end",
        "test04: content_content",
    ]
}


def back_track(p_index, p_data, p_subs):
    while p_index < len(p_data):
        if "begin" in p_data[p_index]:
            name = p_data[p_index].rsplit("_", 1)[0]
            end_idx = p_data.index(name + "_end")
            body = []
            subs = {name: body}
            res = back_track(1, p_data[p_index:end_idx + 1], body)
            p_index = end_idx + 1
            if isinstance(p_subs, list):
                p_subs.append(subs)
            if isinstance(p_subs, dict):
                p_subs.update({name: res})
            continue
        if "end" in p_data[p_index]:
            return p_subs
        if ":" in p_data[p_index]:
            if isinstance(p_subs, list):
                p_subs.append(dict([tuple(p_data[p_index].split(":"))]))
            if isinstance(p_subs, dict):
                p_subs.update(dict([tuple(p_data[p_index].split(":"))]))
            p_index += 1
            continue
        p_subs.append(p_data[p_index])
        p_index += 1
    return p_subs


res_dict = {}
print(back_track(0, data["tracking_info"], res_dict))
import json

print(json.dumps(res_dict))

