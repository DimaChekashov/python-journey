export interface PostData {
  meta: {
    current_page: number;
    per_page: number;
    total_posts: number;
  };
  posts: Post[];
}

export interface Post {
  id: string;
  seo: {
    title: string;
    meta_description: string;
    og_image: string;
    canonical_url: string;
  };
  data: {
    id: number;
    title: string;
    slug: string;
    content: string;
    published_at: string;
    author: string;
    views: number;
  };
  template: PostTemplate;
  status: PostStatus;
}

export enum PostTemplate {
  Blue = "blue",
  Green = "green",
  Red = "red",
}

export enum PostStatus {
  Opened = "opened",
  Closed = "closed",
  Archived = "archived",
}
