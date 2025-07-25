package com.kakaopage.expansion.dao;

import com.kakaopage.expansion.vo.CommentVO;
import java.util.List;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface CommentMapper {
    List<CommentVO> getCommentsFromCommentReplyByBookId(@Param("bookId") Long bookId);
    List<CommentVO> getCommentsFromCommentsByBookId(@Param("bookId") Long bookId);
    void add(CommentVO vo);
    void delete(@Param("commentId") Long commentId);
    List<CommentVO> getByBoard(@Param("boardId") Long boardId);
    List<CommentVO> selectByBoardId(@Param("boardId") Long boardId);
}
