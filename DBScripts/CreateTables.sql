
DROP TABLE IF EXISTS "genres" CASCADE;
CREATE TABLE "genres" (
	"id" serial NOT NULL,
	"name" varchar(100) NOT NULL,
	CONSTRAINT "genres_pk" PRIMARY KEY ("id")
);


DROP TABLE IF EXISTS "artists" CASCADE;
CREATE TABLE "artists" (
	"id" serial NOT NULL,
	"name" varchar(100) NOT NULL,
	CONSTRAINT "artists_pk" PRIMARY KEY ("id")
);


DROP TABLE IF EXISTS "albums" CASCADE;
CREATE TABLE "albums" (
	"id" serial NOT NULL,
	"name" varchar(100) NOT NULL,
	"realease_year" int NOT NULL,
	CONSTRAINT "albums_pk" PRIMARY KEY ("id")
);


DROP TABLE IF EXISTS "tracks" CASCADE;
CREATE TABLE "tracks" (
	"id" serial NOT NULL,
	"album_id" bigint NOT NULL,
	"name" varchar(100) NOT NULL,
	"duration" int NOT NULL,
	CONSTRAINT "tracks_pk" PRIMARY KEY ("id")
);


DROP TABLE IF EXISTS "collections" CASCADE;
CREATE TABLE "collections" (
	"id" serial NOT NULL,
	"name" varchar(100) NOT NULL,
	"realease_year" int NOT NULL,
	CONSTRAINT "collections_pk" PRIMARY KEY ("id")
);


DROP TABLE IF EXISTS "artist_genres" CASCADE;
CREATE TABLE "artist_genres" (
	"id" serial NOT NULL,
	"genre_id" bigint NOT NULL,
	"artist_id" bigint NOT NULL,
	CONSTRAINT "artist_genres_pk" PRIMARY KEY ("id")
);


DROP TABLE IF EXISTS "artist_albums" CASCADE;
CREATE TABLE "artist_albums" (
	"id" serial NOT NULL,
	"artist_id" bigint NOT NULL,
	"album_id" bigint NOT NULL,
	CONSTRAINT "artist_albums_pk" PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "collection_tracks" CASCADE;
CREATE TABLE "collection_tracks" (
	"id" serial NOT NULL,
	"collection_id" bigint NOT NULL,
	"track_id" bigint NOT NULL,
	CONSTRAINT "collection_tracks_pk" PRIMARY KEY ("id")
);

ALTER TABLE "tracks" ADD CONSTRAINT "tracks_album" FOREIGN KEY ("album_id") REFERENCES "albums"("id");

ALTER TABLE "artist_genres" ADD CONSTRAINT "artist_genres_genre" FOREIGN KEY ("genre_id") REFERENCES "genres"("id");
ALTER TABLE "artist_genres" ADD CONSTRAINT "artist_genres_artist" FOREIGN KEY ("artist_id") REFERENCES "artists"("id");

ALTER TABLE "artist_albums" ADD CONSTRAINT "artist_albums_artist" FOREIGN KEY ("artist_id") REFERENCES "artists"("id");
ALTER TABLE "artist_albums" ADD CONSTRAINT "artist_albums_album" FOREIGN KEY ("album_id") REFERENCES "albums"("id");

ALTER TABLE "collection_tracks" ADD CONSTRAINT "collection_tracks_collection" FOREIGN KEY ("collection_id") REFERENCES "collections"("id");
ALTER TABLE "collection_tracks" ADD CONSTRAINT "collection_tracks_track" FOREIGN KEY ("track_id") REFERENCES "tracks"("id");








