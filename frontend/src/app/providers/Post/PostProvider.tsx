import { ReactNode, useState } from "react";
import PostContext from "./PostContext";

export const PostProvider = ({ children }: { children: ReactNode }) => {
  const [status, setStatus] = useState<string>("");

  return (
    <PostContext.Provider value={{ status, setStatus }}>
      {children}
    </PostContext.Provider>
  );
};

export default PostProvider;
