# coding:utf-8
import csv
import os
import jieba
import stylecloud

from module.api import* 

class UserInfo():
    def __init__(self, uid) -> None:
        self.id = uid
        self.name = api_get(f'/user/detail?uid={self.id}').json()['profile']['nickname']
        self.save_rank()

        
        self.write_recommendation()

        # 若无该用户缓存，则爬取评论并生成云图
        file_path = os.path.join(f"rank_data", f"all_rank_data_{self.id}.csv")
        if not os.path.exists(file_path):
            self.get_hot_comment()
            self.generate_wordcloud()

    def get_user_name(self):
        return self.name
    def save_rank(self):
        song_list = self.get_user_rank(0)
        csv_filename = f"all_rank_data_{self.id}.csv"
        field_names = ["Rank", "Playcount", "Song Name", "Song ID", "Artist Names", "Artist IDs", "Album Name", "Album ID"]
        # 写入CSV文件
        self.write_rank(csv_filename, field_names, song_list, 'rank_data')


    def get_user_rank(self,  mode):
        """
        获取用户一周/历史所有的听歌排行记录    
        Args:
            uid: 用户ID
            mode: 1 时返回一周数据，0 时返回所有数据
        """
        try:
            if mode == 0:
                return api_get(f'/user/record?uid={self.id}&type={mode}').json()['allData']
            elif mode == 1:
                return api_get(f'/user/record?uid={self.id}&type={mode}').json()['weekData']
            elif mode == -1:
                api_get(' api_get debug pass')
        except:
            print('User hasn\'t listened music this week!' )



    def write_rank(self, csv_filename, field_names, song_list, folder_path):
        """
        将数据写入CSV文件
        Args:
            csv_filename：文件命名
            field_names: 字段值
            song_list: 想要遍历的 JSON 内容
        """

        # 创建存储文件夹
        os.makedirs(folder_path, exist_ok=True)
        # 写入CSV文件
        csv_filepath = os.path.join(folder_path, csv_filename)
        with open(csv_filepath, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            cnt = 0

            for song in song_list:
                playcount = song["playCount"]
                song_name = song["song"]["name"]
                song_id = song["song"]["id"]
                artists = song["song"]["ar"]
                album_name = song["song"].get("al", {}).get("name", "-")
                album_id = song["song"].get("al", {}).get("id", "-")
                
                artist_names = []
                artist_ids = []
                
                for artist in artists:
                    artist_names.append(artist["name"])
                    artist_ids.append(artist["id"])
                

                cnt += 1
                writer.writerow({
                        "Rank": f"{cnt}",
                        "Playcount": playcount,
                        "Song Name": song_name,
                        "Song ID": song_id,
                        "Artist Names": ", ".join(artist_names),
                        "Artist IDs": ", ".join(map(str, artist_ids)),
                        "Album Name": album_name,
                        "Album ID": album_id
                    })
            
        print("Rank data has been saved to", csv_filepath)


    def read_rank(self, file_path):
        songInfos = []
        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rank = row['Rank']
                playcount = row['Playcount']
                song_name = row['Song Name']
                artist_names = row['Artist Names']
                album_name = row['Album Name'] 
                songInfos.append([rank, song_name, artist_names, album_name, playcount])
        return songInfos
    
    def get_recommendation(self):
        """
        根据风格获取用户的推荐歌曲
        """
        data = api_get(f'/personalized/newsong?limit=20').json()['result']
        return data
    
    def write_recommendation(self):
        """
        将推荐歌曲写入CSV文件
        """
        data = self.get_recommendation()
        csv_filename = f"recommendation_{self.id}.csv"
        field_names = ["Song Name", "Song ID", "Artist Names", "Artist IDs", "Album Name", "Album ID"]
        folder_path = "recommendation_data"

        # 创建存储文件夹
        os.makedirs(folder_path, exist_ok=True)
        # 写入CSV文件
        csv_filepath = os.path.join(folder_path, csv_filename)
        with open(csv_filepath, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()

            for song in data:
                song_name = song["song"]["name"]
                song_id = song["song"]["id"]
                artist_name = song["song"]["artists"][0]["name"]
                artist_id = song["song"]["artists"][0]["id"]
                album_name = song["song"].get("album", {}).get("name", "-")
                album_id = song["song"].get("album", {}).get("id", "-")


                writer.writerow({
                        "Song Name": song_name,
                        "Song ID": song_id,
                        "Artist Names":artist_name,
                        "Artist IDs":artist_id,
                        "Album Name": album_name,
                        "Album ID": album_id
                    })
        print("Recommend data has been saved to", csv_filepath)

    def read_recommendation(self, file_path):
        songInfos = []
        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                album = row['Album Name']
                song_name = row['Song Name']
                artist_names = row['Artist Names']
                songInfos.append([song_name, artist_names, album])
        return songInfos

    def get_song_style(self):
        """
        获取用户曲风偏好的标签
        """
        data = api_get(f'/style/preference').json()
        
        result = []
        tagIDs = []
        if "tagPreferenceVos" in data["data"]:
            tag_preferences = data["data"]["tagPreferenceVos"]
            for preference in tag_preferences:
                tag_name = preference["tagName"]
                ratio = int(preference["ratio"])
                tagIDs.append(preference["tagId"])
                result.append({"value": ratio, "name": tag_name})
        else:
            print("No tag preferences found.")
        return result, tagIDs

    def get_fav_style(self, tagID):
        """
        获取用户喜欢的标签
        """
        
        data = api_get(f'/style/detail?tagId={tagID}').json()

        name = data["data"]["name"]
        desc = data["data"]["desc"]
        template_content = data["data"]["professionalReviews"]["templateContent"]
        pattern = data["data"]["professionalReviews"]["pattern"]

        # 匹配 pattern 中的内容并替换 template_content
        for key, value in pattern.items():
            template_content = template_content.replace("${" + key + "}",  str(value["text"]) )

        # 生成 Markdown 格式的文本
        markdown_text = f"# 你的专属风格为——{name}\n\n - 📑{desc}\n\n - 🎧 {template_content} \n\n * 💖根据你近30天的听歌记录生成，每日更新~"

        return markdown_text


    def get_hot_comment(self, limit = 1):
        """
        获取歌曲热门评论
        """
        songIDs = []
        result = []
        file_path = os.path.join(f"rank_data", f"all_rank_data_{self.id}.csv")

        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                songID = row['Song ID']
                songIDs.append(songID)
        for song_id in songIDs:
            data = api_get(f'/comment/music?id={song_id}&limit={limit}').json()
            hot_comments = data["hotComments"]

            for comment in hot_comments:
                content = comment["content"]
                result.append(content)
            
            print(result)

        # 创建存储评论的文件夹
        folder_name = f"comment"
        os.makedirs(folder_name, exist_ok=True)

        # 将评论内容写入txt文件
        file_path = os.path.join(folder_name, f"comment_{self.id}.txt")
        with open(file_path, "w", encoding="utf-8-sig") as file:
            for comment in result:
                file.write(comment + "\n")

        print(f"评论已保存到 {file_path}")




    def generate_wordcloud(self):
        """
        生成词云图
        """
        file_path = os.path.join(f"comment", f"comment_{self.id}.txt")
        with open(file_path,'r',encoding='utf-8-sig') as f:
            word_list = jieba.cut(f.read())
            result = " ".join(word_list) #分词用空格隔开


        with open('comment\cn_stopwords.txt','r',encoding='utf-8-sig') as f:
            stopwords = f.read().split('\n') #停用词表

        stopwords = set(stopwords) #去重
        stopwords = list(stopwords) #转成list
        stylecloud.gen_stylecloud(
            text=result, # 上面分词的结果作为文本传给text参数
            size=800,
            font_path='msyh.ttc', # 字体设置
            palette='cartocolors.qualitative.Prism_10', # 调色方案选取，从palettable里选择
            gradient='horizontal', # 渐变色方向选了垂直方向
            icon_name='fas fa-comments',  # 蒙版选取，从Font Awesome里选
            custom_stopwords=stopwords, # 停用词设置
            output_name=f'comment\wordcloud_{self.id}.png') # 输出词云图



    def get_user_all_comment_wordcloud(self):
        """
        获取用户所有评论生成词云图
        """
        songIDs = []
        file_path = os.path.join(f"rank_data", f"all_rank_data_{self.id}.csv")
        if not os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    songID = row['Song ID']
                    songIDs.append(songID)
            
            for songID in songIDs:
                self.get_hot_comment(songID, 1)
            self.generate_wordcloud()

user = UserInfo(581065613)
        



