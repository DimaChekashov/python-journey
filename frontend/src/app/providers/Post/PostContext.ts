import { createContext } from "react";

interface PostContextType {
  status: string;
  setStatus: (status: string) => void;
}

const PostContext = createContext<PostContextType>({
  status: "",
  setStatus: () => {},
});

export default PostContext;
