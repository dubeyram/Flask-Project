-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2021 at 09:14 AM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 5.6.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `learn2cod`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(1) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(30) NOT NULL,
  `content` text NOT NULL,
  `tagline` text NOT NULL,
  `img_file` varchar(20) NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `tagline`, `img_file`, `date`) VALUES
(1, 'Why we should learn programming ?.', 'why-we-should-learn-programing', '\r\n<p>Before we discuss this topic in detail we would like to know why you are reading this article. There might be a few reasons and these are:</p>\r\n\r\n<ul>\r\n	<li>You are a non-programmer who wonders how things work in this technical era. You are interested in technology and thinking about to choose this path.</li>\r\n	<li>You are a beginner, just have entered in this field and you have doubts that you took the correct step choosing this field or not. It is scary or frustrating for you or maybe fun for you.</li>\r\n	<li>You are an experienced person and you want to know that after choosing this field how far you have come and what changes you have experienced throughout your journey in programming.</li>\r\n</ul>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>A lot of people before entering into the programming field are curious to know how things work behind the scene? How within a few second Google give us a search result whatever we are looking for? How we are able to connect to someone on facebook around this world? How Google Maps really works to give us direction anywhere in this world? All the above reasons inspire a non-programmer to choose this field. Today we all are dependent on technology in our daily life, for entertainment, for communication, and for everything but very few people know how to read and write code. If you are already coding for years, you will be able to apply this skill beyond your computers. We are surrounded by a lot of problems and coding has given us a lot of solutions in the real world. It doesn&rsquo;t matter if you are a non-programmer, beginner or experienced person, there are multiple reasons you should learn to code.</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><img alt=\"Should Learning Designers Learn to Code? [Poll] | The mLearning ...\" src=\"https://lh3.googleusercontent.com/proxy/GLgajyuLlg6ZK_TKaOpvAIU1osldQtqzyVbCVCuJRXzkyzANWoXOFlnPZG3XmszNqAnfdQg2CyOkYeDExd8uqw9oD97Dk5fN4nsBeMzvdCQi3GkwXHV_HUlgqHfEKXvjeA\" /></p>\r\n\r\n<blockquote>\r\n<p><strong><span style=\"color:#c0392b\">&ldquo;Everybody in this country should learn how to program a computer&hellip; because it teaches you how to think&rdquo;</span></strong><br />\r\n&ndash;<strong>Steve Jobs</strong></p>\r\n</blockquote>\r\n\r\n<h3>1. Attractive Salary and Multiple Career Opportunities:</h3>\r\n\r\n<p>Technology is vast and there are plenty of job opportunities available if you know how to code. Programmers are high in demand all over the world. You can become a freelancer and work freely, you can work for some companies, you can work on your own side projects or you can also use your coding skill for your own startup. The salary of programmers is also attractive because it requires critical thinking and situation analysis. People who are masters in programming work for a few hours but earn more also they are more flexible in their daily lives to do their job. Below is the estimated salary of computer programmers in India.</p>\r\n\r\n<h3>2. Develop Problem-Solving and Logical Skill:</h3>\r\n\r\n<p>Problem-solving skill is the heart of programming and learning programming is about breaking up problems into smaller chunks, using your own logic and algorithms to create a program and then giving a solution for that. Coding forces your brain to think about a problem deeply, organize your thoughts for the same, apply some logic and then providing a solution. Every time you face a new challenge, you need to use your brain, you may have to make your own rule and you need to follow a logical approach.<br />\r\nSo learning and doing programming is an exercise for your brain that eventually improves your problem solving and logical ability. Learning to code will teach you to understand this world, to solve the problems we encounter every day in our life and that is the best thing you can do to change this world. You help people by using computer technologies and you earn respect for that too. You eventually become a smarter person when you see the whole picture of the real-world problem and you solve that using your logical approach.</p>\r\n\r\n<h3>3. Develop Interpersonal Skills:</h3>\r\n\r\n<p>Coding not only improve your technical skill, but it also helps in improving the soft skills. Most of the time when you are working in a team you need to collaborate with other co-workers, you may have to discuss project with them, you need to interact with your manager and all these things eventually develop your soft skill which not only helps in building a good relationship in your professional life but also in personal life. Magic happens in coding when you collaborate with other smart people and build something together that actually something meaningful for people in this world.</p>\r\n\r\n<h3>4. Technologies Are Ruling the World:</h3>\r\n\r\n<p>Technology is embedded everywhere and there is no doubt that it has become a part of our daily life whether it&rsquo;s entertainment or we have to communicate to someone or we have to go somewhere. We are relying on technologies and there are thousands of industries dependent on computer programs to run their business operations. Scientists use computers to analyze and see the results of their experiments and for their own research. It is used in data analysis, finance, food industry, education, customer service, health sector from creating an app or website useful for others to drive a car. It&rsquo;s strange that from morning to evening we are relying on technologies but very few people know how to code.</p>\r\n\r\n<h3>5. Coding is Creativity:</h3>\r\n\r\n<p>Coding is always considered as all about something computational, mathematical, frustrating and boring but there is a creative side of coding as well. When programmers see something is imperfect in this world then it becomes their job to analyze the problem and to give a visionary solution. They see a complete picture of a problem people encounter and they use their creative logical approach to find out the solution for that. Just like painters, a clever programmer picks a suitable programming language, design patterns, patterns of logical expression to implement the solution.</p>\r\n\r\n<h3>6. Understanding of Both Sides of the Equation in Business:</h3>\r\n\r\n<p>In any kind of industry or business, it always becomes difficult for a non-programmer or departments who have to do nothing with coding understanding the complete process that requires to get the job done. A misunderstanding is always developed between engineers and non-programmers when it comes to finding a solution for a specific problem. When you have the coding skill, you can visualize or at least understand the risk, challenges, time from an engineer&rsquo;s point of view. It doesn&rsquo;t matter you are a manager, team leader or marketer in your company if you know about coding, you understand both sides of the table. You are able to tackle the problems smoothly and that&rsquo;s very important to run a business successfully.</p>\r\n\r\n<h3>7. Empowering and Life-Changing Experience:</h3>\r\n\r\n<p>Programming always gives you a new challenge where you have to take the risk every time and that teaches you to take the risk in your life too. The world is full of software, apps, website and when you build these things on your own you feel more confident and powerful. When a programmer is able to solve a problem that had no solution before it becomes a life-changing experience for them.</p>\r\n\r\n<blockquote>\r\n<p><strong><span style=\"color:#e67e22\">Whether you want to uncover the secrets of the universe, or you just want to pursue a career in the 21st century, basic computer programming is an essential skill to learn.</span></strong><br />\r\n&ndash;&nbsp;<strong>Stephen Hawking</strong></p>\r\n</blockquote>\r\n\r\n<blockquote>\r\n<p style=\"text-align:justify\"><span style=\"font-size:24px\"><span style=\"color:#2ecc71\"><strong>&nbsp;Having a background in mathematics or computer science is not a requirement these days for those interested in coding. Read more to find out why you should learn&nbsp; programming!</strong></span></span></p>\r\n</blockquote>\r\n', 'Programming | Technology', 'post1.png', '2020-07-11'),
(2, 'What are the things I should know before I start learning programming? ', 'thing-should-know-befor-start-', '<p>Depending on how deep you want to get into it, these things can be useful.</p>\r\n\r\n<p>1) Boolean algebra (Logic) That&#39;s really important.</p>\r\n\r\n<p>2) Basics of computer hardware. (e.g. what is a bit, a byte, an address bus, a data bus...) Knowing how things work in the actual machine can help you understand what you can and can&#39;t do in a program.</p>\r\n\r\n<p>3) Binary (and optionally Hexadecimal)</p>\r\n\r\n<p>Ultimately, you have to find the way that works best for you regarding how to learn programming.</p>\r\n\r\n<p>If you like to get involved immediately, do concrete stuff, then just learn while coding. (that&#39;s generally the best way to learn a&nbsp;language)</p>\r\n\r\n<p>If you prefer having a good grasp at the basics before jumping in, then read a book about it.</p>\r\n\r\n<p>Just remember that when you learn by coding, you&#39;re only gonna learn the aspects of programming used in the language you&#39;re coding with, whereas when you read a book about programming in general, you&#39;ll learn about the main concepts of programming that are common to most languages.</p>\r\n\r\n<p>For instance, if you learn with lua, you won&#39;t learn what&#39;s in Java, because they&#39;re two very different languages that serve very different goals.<br />\r\nBut if you read a book that explains programming in general with little to no code in it, you&#39;ll know how to program, but you won&#39;t know how to code.</p>\r\n\r\n', 'Beginners | Programming', 'post1.png', '2020-07-11');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `name` text NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(320) NOT NULL,
  `pasword` varchar(50) NOT NULL,
  `img` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`name`, `username`, `email`, `pasword`, `img`) VALUES
('RamGopal Dubey', 'dubey', 'dubey233310@gmail.com', 'sha256$AdfCodjZRj8peg8M$364c43126e5f6126ba19c2de75', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`) USING BTREE;

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
